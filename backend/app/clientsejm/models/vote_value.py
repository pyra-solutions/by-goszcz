from enum import Enum


class VoteValue(str, Enum):
    ABSENT = "ABSENT"
    ABSTAIN = "ABSTAIN"
    NO = "NO"
    NO_VOTE = "NO_VOTE"
    PRESENT = "PRESENT"
    VOTE_INVALID = "VOTE_INVALID"
    VOTE_VALID = "VOTE_VALID"
    YES = "YES"

    def __str__(self) -> str:
        return str(self.value)
