import yfinance as yf
import pandas as pd

# List of stocks to scan
tickers = ['AAPL', 'MSFT', 'TSLA', 'JPM', 'GS']

print("--- Running Advanced Algorithmic Screener (EMA & Volume) ---\n")

for ticker in tickers:
    try:
        # 1. Download the last 1 year of daily stock data
        stock = yf.Ticker(ticker)
        df = stock.history(period="1y")
        
        # 2. Calculate Exponential Moving Averages (EMA)
        # EMA puts exponentially more weight on recent price action than SMA
        df['50_EMA'] = df['Close'].ewm(span=50, adjust=False).mean()
        df['200_EMA'] = df['Close'].ewm(span=200, adjust=False).mean()
        
        # 3. Calculate 20-Day Average Volume
        df['20_Vol_Avg'] = df['Volume'].rolling(window=20).mean()
        
        # 4. Get the most recent day's data
        latest = df.iloc[-1]
        
        # 5. Trend and Volume Logic
        trend_bullish = latest['50_EMA'] > latest['200_EMA']
        volume_breakout = latest['Volume'] > latest['20_Vol_Avg']
        
        # 6. Signal Output Logic
        if trend_bullish and volume_breakout:
            print(f"[STRONG BUY] {ticker}: 50-EMA > 200-EMA AND high volume breakout detected.")
        elif trend_bullish and not volume_breakout:
            print(f"[WEAK BUY]   {ticker}: 50-EMA > 200-EMA, but lacks volume confirmation.")
        else:
            print(f"[HOLD/SELL]  {ticker}: Bearish trend (50-EMA is below 200-EMA).")
            
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
