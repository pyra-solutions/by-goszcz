from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.voting_kind import VotingKind
from ..models.voting_majority import VotingMajority
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vote import Vote
    from ..models.voting_option import VotingOption


T = TypeVar("T", bound="VotingDetails")


@_attrs_define
class VotingDetails:
    """a voting with results

    Attributes:
        yes (int | Unset): number of 'yes' votes Example: 209.
        no (int | Unset): number of 'no' votes Example: 17.
        abstain (int | Unset): number of 'abstain' votes Example: 4.
        not_participating (int | Unset): number of people who did not vote Example: 1.
        term (int | Unset): a Sejm term Example: 9.
        sitting (int | Unset): a Sejm sitting number Example: 62.
        sitting_day (int | Unset): a day of Sejm sitting Example: 1.
        voting_number (int | Unset): a voting number Example: 43.
        date (datetime.datetime | Unset): a voting date and time Example: 2022-09-29 15:56:30.
        title (str | Unset): a voting title Example: Pkt. 27 Sprawozdanie Komisji o rządowym projekcie ustawy o zmianie
            ustawy - Prawo energetyczne oraz ustawy o odnawialnych źródłach energii (druki nr 2634, 2644 i 2644-A).
        description (str | Unset): description Example: a description of a voting.
        topic (str | Unset): a voting topic Example: głosowanie nad całością projektu.
        kind (VotingKind | Unset):
        majority_type (VotingMajority | Unset):
        majority_votes (int | Unset): number of votes that constitute a majority
        voting_options (list[VotingOption] | Unset): a list of options when voting on a list
        total_voted (int | Unset): number of people who voted Example: 459.
        against_all (int | Unset): number of votes against all options when voting on list
        links (list[Any] | Unset): Links
        present (int | Unset): number of 'present' votes in quorum voting Example: 460.
        votes (list[Vote] | Unset): a list of votes
    """

    yes: int | Unset = UNSET
    no: int | Unset = UNSET
    abstain: int | Unset = UNSET
    not_participating: int | Unset = UNSET
    term: int | Unset = UNSET
    sitting: int | Unset = UNSET
    sitting_day: int | Unset = UNSET
    voting_number: int | Unset = UNSET
    date: datetime.datetime | Unset = UNSET
    title: str | Unset = UNSET
    description: str | Unset = UNSET
    topic: str | Unset = UNSET
    kind: VotingKind | Unset = UNSET
    majority_type: VotingMajority | Unset = UNSET
    majority_votes: int | Unset = UNSET
    voting_options: list[VotingOption] | Unset = UNSET
    total_voted: int | Unset = UNSET
    against_all: int | Unset = UNSET
    links: list[Any] | Unset = UNSET
    present: int | Unset = UNSET
    votes: list[Vote] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        yes = self.yes

        no = self.no

        abstain = self.abstain

        not_participating = self.not_participating

        term = self.term

        sitting = self.sitting

        sitting_day = self.sitting_day

        voting_number = self.voting_number

        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        title = self.title

        description = self.description

        topic = self.topic

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        majority_type: str | Unset = UNSET
        if not isinstance(self.majority_type, Unset):
            majority_type = self.majority_type.value

        majority_votes = self.majority_votes

        voting_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.voting_options, Unset):
            voting_options = []
            for voting_options_item_data in self.voting_options:
                voting_options_item = voting_options_item_data.to_dict()
                voting_options.append(voting_options_item)

        total_voted = self.total_voted

        against_all = self.against_all

        links: list[Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links

        present = self.present

        votes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.votes, Unset):
            votes = []
            for votes_item_data in self.votes:
                votes_item = votes_item_data.to_dict()
                votes.append(votes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if yes is not UNSET:
            field_dict["yes"] = yes
        if no is not UNSET:
            field_dict["no"] = no
        if abstain is not UNSET:
            field_dict["abstain"] = abstain
        if not_participating is not UNSET:
            field_dict["notParticipating"] = not_participating
        if term is not UNSET:
            field_dict["term"] = term
        if sitting is not UNSET:
            field_dict["sitting"] = sitting
        if sitting_day is not UNSET:
            field_dict["sittingDay"] = sitting_day
        if voting_number is not UNSET:
            field_dict["votingNumber"] = voting_number
        if date is not UNSET:
            field_dict["date"] = date
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if topic is not UNSET:
            field_dict["topic"] = topic
        if kind is not UNSET:
            field_dict["kind"] = kind
        if majority_type is not UNSET:
            field_dict["majorityType"] = majority_type
        if majority_votes is not UNSET:
            field_dict["majorityVotes"] = majority_votes
        if voting_options is not UNSET:
            field_dict["votingOptions"] = voting_options
        if total_voted is not UNSET:
            field_dict["totalVoted"] = total_voted
        if against_all is not UNSET:
            field_dict["againstAll"] = against_all
        if links is not UNSET:
            field_dict["links"] = links
        if present is not UNSET:
            field_dict["present"] = present
        if votes is not UNSET:
            field_dict["votes"] = votes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vote import Vote
        from ..models.voting_option import VotingOption

        d = dict(src_dict)
        yes = d.pop("yes", UNSET)

        no = d.pop("no", UNSET)

        abstain = d.pop("abstain", UNSET)

        not_participating = d.pop("notParticipating", UNSET)

        term = d.pop("term", UNSET)

        sitting = d.pop("sitting", UNSET)

        sitting_day = d.pop("sittingDay", UNSET)

        voting_number = d.pop("votingNumber", UNSET)

        _date = d.pop("date", UNSET)
        date: datetime.datetime | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date)

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        topic = d.pop("topic", UNSET)

        _kind = d.pop("kind", UNSET)
        kind: VotingKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = VotingKind(_kind)

        _majority_type = d.pop("majorityType", UNSET)
        majority_type: VotingMajority | Unset
        if isinstance(_majority_type, Unset):
            majority_type = UNSET
        else:
            majority_type = VotingMajority(_majority_type)

        majority_votes = d.pop("majorityVotes", UNSET)

        _voting_options = d.pop("votingOptions", UNSET)
        voting_options: list[VotingOption] | Unset = UNSET
        if _voting_options is not UNSET:
            voting_options = []
            for voting_options_item_data in _voting_options:
                voting_options_item = VotingOption.from_dict(voting_options_item_data)

                voting_options.append(voting_options_item)

        total_voted = d.pop("totalVoted", UNSET)

        against_all = d.pop("againstAll", UNSET)

        links = cast(list[Any], d.pop("links", UNSET))

        present = d.pop("present", UNSET)

        _votes = d.pop("votes", UNSET)
        votes: list[Vote] | Unset = UNSET
        if _votes is not UNSET:
            votes = []
            for votes_item_data in _votes:
                votes_item = Vote.from_dict(votes_item_data)

                votes.append(votes_item)

        voting_details = cls(
            yes=yes,
            no=no,
            abstain=abstain,
            not_participating=not_participating,
            term=term,
            sitting=sitting,
            sitting_day=sitting_day,
            voting_number=voting_number,
            date=date,
            title=title,
            description=description,
            topic=topic,
            kind=kind,
            majority_type=majority_type,
            majority_votes=majority_votes,
            voting_options=voting_options,
            total_voted=total_voted,
            against_all=against_all,
            links=links,
            present=present,
            votes=votes,
        )

        voting_details.additional_properties = d
        return voting_details

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
