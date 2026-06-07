from datetime import datetime

from src.interfaces.data_source import DataSource

from src.candles.time_candle.time_candle import TimeCandle

from src.data.timeframe import Timeframe

from src.candles.time_candle.generator import (
    TimeCandleGenerator
)


class TimeCandles:

    def __init__(
        self,
        provider_name: str
    ):
        self.data_source = DataSource(
            provider_name
        )

        self.generator = (
            TimeCandleGenerator()
        )

    def get_candles(
        self,
        symbol: str,
        timeframe: Timeframe,
        start: datetime,
        end: datetime
    ) -> list[TimeCandle]:

        market_data = (
            self.data_source.get_data(
                symbol,
                timeframe,
                start,
                end
            )
        )

        return self.generator.generate(
            market_data
        )
