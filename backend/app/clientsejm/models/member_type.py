from enum import Enum


class MemberType(str, Enum):
    CHAIRMAN = "chairman"
    CO_CHAIRMAN = "co_chairman"
    DEPUTY_CHAIRMAN = "deputy_chairman"
    MEMBER = "member"
    SECRETARY = "secretary"

    def __str__(self) -> str:
        return str(self.value)
