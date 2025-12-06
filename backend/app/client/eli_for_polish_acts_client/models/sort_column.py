from enum import Enum


class SortColumn(str, Enum):
    CHANGE = "change"
    POSITION = "position"
    PUBLISHER = "publisher"
    TITLE = "title"

    def __str__(self) -> str:
        return str(self.value)
