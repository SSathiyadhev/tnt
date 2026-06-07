from datetime import datetime

from src.data.market_data_point import MarketDataPoint
from src.data.timeframe import Timeframe

from src.data.providers import PROVIDERS


class DataSource:

    def __init__(
        self,
        provider_name: str
    ):

        self.providers = {
            provider.name: provider
            for provider in PROVIDERS
        }

        self.provider = self.providers[
            provider_name
        ]

    def get_available_providers(
        self
    ) -> list[str]:

        return list(
            self.providers.keys()
        )

    def get_data(
        self,
        symbol: str,
        timeframe: Timeframe,
        start: datetime,
        end: datetime
    ) -> list[MarketDataPoint]:

        return self.provider.get_data(
            symbol,
            timeframe,
            start,
            end
        )
