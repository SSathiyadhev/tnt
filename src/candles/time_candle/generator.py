from src.candles.time_candle.time_candle import TimeCandle
from src.data.market_data_point import MarketDataPoint


class TimeCandleGenerator:

    def generate(
        self,
        market_data: list[MarketDataPoint]
    ) -> list[TimeCandle]:

        candles = []

        for point in market_data:

            candles.append(
                TimeCandle(
                    timestamp=point.timestamp,
                    open=point.open,
                    high=point.high,
                    low=point.low,
                    close=point.close
                )
            )

        return candles
