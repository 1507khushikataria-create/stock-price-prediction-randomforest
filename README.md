# stock-price-prediction-randomforest# Stock Price Prediction using Machine Learning (Random Forest)

## Project Overview

This project demonstrates how machine learning can be used to analyze historical stock market data and predict stock prices. The goal is to build a regression model that learns patterns from past stock prices and predicts the closing price based on other features such as open price, high price, low price, and trading volume.

The project uses the **Random Forest Regressor**, a powerful ensemble machine learning algorithm that combines multiple decision trees to produce more accurate and stable predictions.

This project also includes **data cleaning, visualization, feature preparation, model training, and evaluation**.

---

# Dataset

The dataset used in this project is a historical stock price dataset named:

**HistoricalQuotes.csv**

It contains daily stock market data with the following columns:

| Column     | Description              |
| ---------- | ------------------------ |
| Date       | Trading date             |
| Close/Last | Closing stock price      |
| Volume     | Number of shares traded  |
| Open       | Opening stock price      |
| High       | Highest price of the day |
| Low        | Lowest price of the day  |

Example data:

| Date       | Close/Last | Volume    | Open    | High    | Low |
| ---------- | ---------- | --------- | ------- | ------- | --- |
| 02/28/2020 | $273.36    | 106721200 | $257.26 | $278.41 | $2  |
