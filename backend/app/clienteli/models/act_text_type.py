from enum import Enum


class ActTextType(str, Enum):
    H = "H"
    I = "I"
    O = "O"
    T = "T"
    U = "U"

    def __str__(self) -> str:
        return str(self.value)
