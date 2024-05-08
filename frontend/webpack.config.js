const miniCssExtractPlugin = require('mini-css-extract-plugin')
const path = require('path');

module.exports = {
  mode: 'production',
  entry: './src/js/index.js',
  output: {
    filename: 'main.js',
    path: path.resolve(__dirname, '../static/dist/js'),
  },
  plugins: [new miniCssExtractPlugin({filename: '../css/main.css'})],
  module: {
    rules: [
        {
            test: /\.(scss)$/,
            use: [miniCssExtractPlugin.loader, 'css-loader', 'sass-loader']
        }
    ]
  }
};