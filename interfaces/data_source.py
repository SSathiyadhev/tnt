from datetime import datetime

from data.market_data_point import MarketDataPoint
from data.timeframe import Timeframe


class DataSource:

    def __init__(self):
        self.provider = None

    def set_provider(
        self,
        provider
    ):
        self.provider = provider

    def get_data(
        self,
        symbol: str,
        timeframe: Timeframe,
        start: datetime,
        end: datetime
    ) -> list[MarketDataPoint]:

        if self.provider is None:
            raise RuntimeError(
                "No data provider selected."
            )

        return self.provider.get_data(
            symbol,
            timeframe,
            start,
            end
        )
