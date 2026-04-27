# 阶段1：构建前端
FROM node:20-alpine AS frontend-builder

WORKDIR /app/frontend
COPY frontend/package*.json ./
RUN npm install
COPY frontend/ .
RUN npm run build

# 阶段2：Python 后端环境
FROM python:3.11-slim AS backend

WORKDIR /app/backend
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/ .

# 阶段3：最终运行环境（Nginx + Python）
FROM python:3.11-slim

# 更换国内源并安装 Nginx
RUN sed -i 's/deb.debian.org/mirrors.aliyun.com/g' /etc/apt/sources.list.d/debian.sources \
    && sed -i 's/security.debian.org/mirrors.aliyun.com/g' /etc/apt/sources.list.d/debian.sources \
    && apt-get update \
    && apt-get install -y nginx --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# 复制后端
COPY --from=backend /app/backend /app/backend
COPY --from=backend /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=backend /usr/local/bin /usr/local/bin

# 复制前端构建产物
COPY --from=frontend-builder /app/frontend/dist /usr/share/nginx/html

# 写入 Nginx 配置
RUN printf '%s\n' \
    'server {' \
    '    listen 80;' \
    '    server_name localhost;' \
    '    root /usr/share/nginx/html;' \
    '    index index.html;' \
    '' \
    '    location / {' \
    '        try_files $uri $uri/ /index.html;' \
    '    }' \
    '' \
    '    location /api/ {' \
    '        proxy_pass http://localhost:8000/api/;' \
    '        proxy_set_header Host $host;' \
    '        proxy_set_header X-Real-IP $remote_addr;' \
    '        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;' \
    '        proxy_set_header X-Forwarded-Proto $scheme;' \
    '    }' \
    '}' > /etc/nginx/conf.d/default.conf

# 写入启动脚本
RUN printf '%s\n' \
    '#!/bin/bash' \
    '' \
    '# 启动后端' \
    'cd /app/backend && python run.py &' \
    '' \
    '# 启动 Nginx' \
    'nginx -g "daemon off;"' > /app/start.sh \
    && chmod +x /app/start.sh

EXPOSE 80 8000

CMD ["/app/start.sh"]
