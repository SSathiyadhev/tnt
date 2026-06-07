import yfinance as yf

from datetime import datetime

from src.data.market_data_point import MarketDataPoint
from src.data.timeframe import Timeframe


class YahooDataSource:

    def get_data(
        self,
        symbol: str,
        timeframe: Timeframe,
        start: datetime,
        end: datetime
    ) -> list[MarketDataPoint]:

        raw_data = yf.download(
            symbol,
            start=start,
            end=end,
            interval=str(timeframe)
        )

        raw_data.columns = raw_data.columns.droplevel(1)

        market_data = []

        for timestamp, row in raw_data.iterrows():

            market_data.append(
                MarketDataPoint(
                    timestamp=timestamp,
                    open=float(row["Open"]),
                    high=float(row["High"]),
                    low=float(row["Low"]),
                    close=float(row["Close"]),
                    volume=float(row["Volume"])
                )
            )

        return market_data
