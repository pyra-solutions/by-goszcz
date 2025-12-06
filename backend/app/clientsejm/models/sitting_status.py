from enum import Enum


class SittingStatus(str, Enum):
    CANCELLED = "CANCELLED"
    FINISHED = "FINISHED"
    PLANNED = "PLANNED"

    def __str__(self) -> str:
        return str(self.value)
