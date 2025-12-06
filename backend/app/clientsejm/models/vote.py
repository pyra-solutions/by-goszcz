from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.vote_value import VoteValue
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vote_list_votes import VoteListVotes


T = TypeVar("T", bound="Vote")


@_attrs_define
class Vote:
    """a vote

    Attributes:
        mp (int | Unset): an MP number Example: 43.
        first_name (str | Unset): an MP first name Example: Jan.
        last_name (str | Unset): an MP last name Example: Kowalski.
        second_name (str | Unset): an MP second name Example: Krzysztof.
        club (str | Unset): an MP club Example: PiS.
        vote (VoteValue | Unset):
        list_votes (VoteListVotes | Unset): a vote on a list
        m_p (int | Unset):
    """

    mp: int | Unset = UNSET
    first_name: str | Unset = UNSET
    last_name: str | Unset = UNSET
    second_name: str | Unset = UNSET
    club: str | Unset = UNSET
    vote: VoteValue | Unset = UNSET
    list_votes: VoteListVotes | Unset = UNSET
    m_p: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mp = self.mp

        first_name = self.first_name

        last_name = self.last_name

        second_name = self.second_name

        club = self.club

        vote: str | Unset = UNSET
        if not isinstance(self.vote, Unset):
            vote = self.vote.value

        list_votes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.list_votes, Unset):
            list_votes = self.list_votes.to_dict()

        m_p = self.m_p

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mp is not UNSET:
            field_dict["MP"] = mp
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if second_name is not UNSET:
            field_dict["secondName"] = second_name
        if club is not UNSET:
            field_dict["club"] = club
        if vote is not UNSET:
            field_dict["vote"] = vote
        if list_votes is not UNSET:
            field_dict["listVotes"] = list_votes
        if m_p is not UNSET:
            field_dict["mP"] = m_p

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vote_list_votes import VoteListVotes

        d = dict(src_dict)
        mp = d.pop("MP", UNSET)

        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        second_name = d.pop("secondName", UNSET)

        club = d.pop("club", UNSET)

        _vote = d.pop("vote", UNSET)
        vote: VoteValue | Unset
        if isinstance(_vote, Unset):
            vote = UNSET
        else:
            vote = VoteValue(_vote)

        _list_votes = d.pop("listVotes", UNSET)
        list_votes: VoteListVotes | Unset
        if isinstance(_list_votes, Unset):
            list_votes = UNSET
        else:
            list_votes = VoteListVotes.from_dict(_list_votes)

        m_p = d.pop("mP", UNSET)

        vote = cls(
            mp=mp,
            first_name=first_name,
            last_name=last_name,
            second_name=second_name,
            club=club,
            vote=vote,
            list_votes=list_votes,
            m_p=m_p,
        )

        vote.additional_properties = d
        return vote

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
