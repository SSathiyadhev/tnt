from datetime import datetime


class TimeCandle:

    def __init__(
        self,
        timestamp: datetime,
        open: float,
        high: float,
        low: float,
        close: float
    ):
        self.timestamp = timestamp

        self.open = open
        self.high = high
        self.low = low
        self.close = close

    def __str__(self) -> str:
        return (
            f"TimeCandle("
            f"timestamp={self.timestamp}, "
            f"open={self.open:.2f}, "
            f"high={self.high:.2f}, "
            f"low={self.low:.2f}, "
            f"close={self.close:.2f}"
            f")"
        )
