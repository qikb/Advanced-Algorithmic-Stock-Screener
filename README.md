# Advanced Algorithmic Stock Screener

This project is an automated quantitative screening tool built with Python, `yfinance`, and `pandas` to identify bullish market trend reversals and filter out false-positive momentum signals.

## The Objective
To identify large-cap equities (e.g., AAPL, MSFT, TSLA, JPM, GS) that are entering a confirmed bullish trend. Moving beyond standard lagging indicators, this screener utilizes Exponential Moving Averages (EMA) for faster price responsiveness and integrates a dynamic Volume Confirmation filter to ensure breakouts are supported by institutional liquidity.

## How It Works
1. **Data Aggregation:** Pulls the last 1 year of daily historical pricing and volume data via the Yahoo Finance API.
2. **Trend Analysis (EMA):** Calculates the 50-day and 200-day Exponential Moving Averages to identify the Golden Cross, applying heavier mathematical weight to recent price action compared to a standard Simple Moving Average (SMA).
3. **Volume Confirmation:** Computes a 20-day rolling average of trading volume to gauge market participation.
4. **Signal Generation:** Evaluates the convergence of trend and liquidity to output an automated, tiered recommendation:
   - `[STRONG BUY]` : 50-EMA > 200-EMA AND current volume exceeds the 20-day average.
   - `[WEAK BUY]` : Bullish trend is present, but lacks the trading volume to confirm a safe entry.
   - `[HOLD/SELL]` : Bearish trend (50-EMA < 200-EMA).
