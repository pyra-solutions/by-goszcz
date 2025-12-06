from enum import Enum


class SearchDate(str, Enum):
    AFTER = "AFTER"
    BEFORE = "BEFORE"
    BETWEEN = "BETWEEN"
    NONE = "NONE"
    ON_DAY = "ON_DAY"

    def __str__(self) -> str:
        return str(self.value)
