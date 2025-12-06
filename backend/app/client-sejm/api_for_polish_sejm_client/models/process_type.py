from enum import Enum


class ProcessType(str, Enum):
    BILL = "BILL"
    CONSTITUTIONAL_TRIBUNAL_RULING = "CONSTITUTIONAL_TRIBUNAL_RULING"
    DRAFT_RESOLUTION = "DRAFT_RESOLUTION"
    OTHER = "OTHER"

    def __str__(self) -> str:
        return str(self.value)
