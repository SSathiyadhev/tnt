from datetime import datetime


class MarketDataPoint:

    def __init__(
        self,
        timestamp: datetime,
        open: float,
        high: float,
        low: float,
        close: float,
        volume: float
    ):
        self.timestamp = timestamp

        self.open = open
        self.high = high
        self.low = low
        self.close = close

        self.volume = volume

    def __str__(self) -> str:
        return (
            f"MarketDataPoint("
            f"timestamp={self.timestamp}, "
            f"open={self.open:.2f}, "
            f"high={self.high:.2f}, "
            f"low={self.low:.2f}, "
            f"close={self.close:.2f}, "
            f"volume={self.volume}"
            f")"
        )
