from datetime import datetime

from src.interfaces.data_source import DataSource
from src.data.providers.yahoo import YahooDataSource
from src.data.timeframe import Timeframe, TimeUnit


data_source = DataSource()

data_source.set_provider(
    YahooDataSource()
)

data = data_source.get_data(
    symbol="AAPL",
    timeframe=Timeframe(1, TimeUnit.DAY),
    start=datetime(2025, 1, 1),
    end=datetime(2025, 2, 1)
)

print(data[0])
