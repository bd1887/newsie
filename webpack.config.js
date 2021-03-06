var path = require("path");
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');

module.exports = {
  context: __dirname,

  entry: './frontend/static/js/index',

  output: {
      path: path.resolve('./frontend/static/bundles/'),
      filename: "[name]-[hash].js",
  },

  plugins: [
    new BundleTracker({filename: './frontend/webpack-stats.json'}),
  ],
  module: {
    rules: [
        {
            test: /\.jsx?$/,
            exclude: /node_modules/,
            use: [
                {
                loader: 'babel-loader',
                options: {
                    presets: ['@babel/react']
                }
                }
            ],
        },
        {
          test: /\.css$/,
          use: [
            'style-loader',
            'css-loader'
          ]
        },
    ],
  },
  resolve: {
    extensions: ['*', '.js', '.jsx']
  }

};