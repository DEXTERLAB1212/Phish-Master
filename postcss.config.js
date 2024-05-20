module.exports = {
  plugins: [
    require('@fullhuman/postcss-purgecss')({
      content: [
        './templates/**/*.html',
        './static/**/*.js',
      ],
      defaultExtractor: content => content.match(/[\w-/:]+(?<!:)/g) || []
    })
  ]
}
