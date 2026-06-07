from enum import Enum


class TimeUnit(Enum):
    SECOND = "s"
    MINUTE = "m"
    HOUR = "h"
    DAY = "d"
    WEEK = "w"
    MONTH = "mo"


class Timeframe:

    def __init__(
        self,
        value: int,
        unit: TimeUnit
    ):
        self.value = value
        self.unit = unit

    def __str__(self) -> str:
        return f"{self.value}{self.unit.value}"
