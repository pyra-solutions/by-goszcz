from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.vote_value import VoteValue
from ..models.voting_kind import VotingKind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vote_mp_list_votes import VoteMPListVotes


T = TypeVar("T", bound="VoteMP")


@_attrs_define
class VoteMP:
    """a vote used in MP votings

    Attributes:
        voting_number (int | Unset): a voting number Example: 43.
        date (datetime.datetime | Unset): a voting date and time Example: 2022-09-29 15:56:30.
        kind (VotingKind | Unset):
        title (str | Unset): a voting title Example: Pkt. 27 Sprawozdanie Komisji o rządowym projekcie ustawy o zmianie
            ustawy - Prawo energetyczne oraz ustawy o odnawialnych źródłach energii (druki nr 2634, 2644 i 2644-A).
        description (str | Unset): description Example: a description of a voting.
        topic (str | Unset): a voting topic Example: głosowanie nad całością projektu.
        vote (VoteValue | Unset):
        list_votes (VoteMPListVotes | Unset): 'yes' votes on a list
    """

    voting_number: int | Unset = UNSET
    date: datetime.datetime | Unset = UNSET
    kind: VotingKind | Unset = UNSET
    title: str | Unset = UNSET
    description: str | Unset = UNSET
    topic: str | Unset = UNSET
    vote: VoteValue | Unset = UNSET
    list_votes: VoteMPListVotes | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        voting_number = self.voting_number

        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        title = self.title

        description = self.description

        topic = self.topic

        vote: str | Unset = UNSET
        if not isinstance(self.vote, Unset):
            vote = self.vote.value

        list_votes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.list_votes, Unset):
            list_votes = self.list_votes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if voting_number is not UNSET:
            field_dict["votingNumber"] = voting_number
        if date is not UNSET:
            field_dict["date"] = date
        if kind is not UNSET:
            field_dict["kind"] = kind
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if topic is not UNSET:
            field_dict["topic"] = topic
        if vote is not UNSET:
            field_dict["vote"] = vote
        if list_votes is not UNSET:
            field_dict["listVotes"] = list_votes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vote_mp_list_votes import VoteMPListVotes

        d = dict(src_dict)
        voting_number = d.pop("votingNumber", UNSET)

        _date = d.pop("date", UNSET)
        date: datetime.datetime | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date)

        _kind = d.pop("kind", UNSET)
        kind: VotingKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = VotingKind(_kind)

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        topic = d.pop("topic", UNSET)

        _vote = d.pop("vote", UNSET)
        vote: VoteValue | Unset
        if isinstance(_vote, Unset):
            vote = UNSET
        else:
            vote = VoteValue(_vote)

        _list_votes = d.pop("listVotes", UNSET)
        list_votes: VoteMPListVotes | Unset
        if isinstance(_list_votes, Unset):
            list_votes = UNSET
        else:
            list_votes = VoteMPListVotes.from_dict(_list_votes)

        vote_mp = cls(
            voting_number=voting_number,
            date=date,
            kind=kind,
            title=title,
            description=description,
            topic=topic,
            vote=vote,
            list_votes=list_votes,
        )

        vote_mp.additional_properties = d
        return vote_mp

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
