from datetime import datetime

from src.interfaces import DataSource
from src.interfaces import candles

from src.data.timeframe import (
    Timeframe,
    TimeUnit
)


print("=== Data Source API ===")

data_source = DataSource(
    "Yahoo"
)

market_data = data_source.get_data(
    symbol="AAPL",
    timeframe=Timeframe(
        1,
        TimeUnit.DAY
    ),
    start=datetime(2025, 1, 1),
    end=datetime(2025, 2, 1)
)

print(market_data[0])


print("\n=== Candle API ===")

time_candles = candles.TimeCandles(
    "Yahoo"
)

candle_data = time_candles.get_candles(
    symbol="AAPL",
    timeframe=Timeframe(
        1,
        TimeUnit.DAY
    ),
    start=datetime(2025, 1, 1),
    end=datetime(2025, 2, 1)
)

print(candle_data[0])

print(
    "Close Price:",
    candle_data[0].close
)
