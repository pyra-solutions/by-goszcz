from enum import Enum


class StatusInForce(str, Enum):
    IN_FORCE = "IN_FORCE"
    NOT_IN_FORCE = "NOT_IN_FORCE"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
