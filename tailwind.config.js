/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: '#FFD93D',
        secondary: '#6BCBFF',
        accent: '#FF8B94',
        warm: '#FFF5E4',
        soft: '#E8F4F8'
      }
    },
  },
  plugins: [],
}
