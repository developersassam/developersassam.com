/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/content/**/*.html', 
    './templates/elements/**/*.html', 
    './templates/elements/*.html', 
    './templates/content/*.html' , 
    './templates/content/**/*.md',
    "./src/markdown_page.py",
    "./templates/base.html",
    "./templates/tailwind_include.txt"
  ],
  theme: {
    borderWidth: {
      '3' : '3px'
    },
    extend: {},
  },
  plugins: [],
}

