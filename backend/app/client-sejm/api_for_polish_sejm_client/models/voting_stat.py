from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="VotingStat")


@_attrs_define
class VotingStat:
    """MP voting statistics

    Attributes:
        sitting (int | Unset): sitting number
        date (datetime.date | Unset): sitting date Example: 2022-03-10.
        num_votings (int | Unset): number of votings on this day
        num_voted (int | Unset): number of MP votings on this day
        num_missed (int | Unset): number of votings missed on this day
        absence_excuse (bool | Unset): is there a excuse for absence
    """

    sitting: int | Unset = UNSET
    date: datetime.date | Unset = UNSET
    num_votings: int | Unset = UNSET
    num_voted: int | Unset = UNSET
    num_missed: int | Unset = UNSET
    absence_excuse: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sitting = self.sitting

        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        num_votings = self.num_votings

        num_voted = self.num_voted

        num_missed = self.num_missed

        absence_excuse = self.absence_excuse

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sitting is not UNSET:
            field_dict["sitting"] = sitting
        if date is not UNSET:
            field_dict["date"] = date
        if num_votings is not UNSET:
            field_dict["numVotings"] = num_votings
        if num_voted is not UNSET:
            field_dict["numVoted"] = num_voted
        if num_missed is not UNSET:
            field_dict["numMissed"] = num_missed
        if absence_excuse is not UNSET:
            field_dict["absenceExcuse"] = absence_excuse

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sitting = d.pop("sitting", UNSET)

        _date = d.pop("date", UNSET)
        date: datetime.date | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()

        num_votings = d.pop("numVotings", UNSET)

        num_voted = d.pop("numVoted", UNSET)

        num_missed = d.pop("numMissed", UNSET)

        absence_excuse = d.pop("absenceExcuse", UNSET)

        voting_stat = cls(
            sitting=sitting,
            date=date,
            num_votings=num_votings,
            num_voted=num_voted,
            num_missed=num_missed,
            absence_excuse=absence_excuse,
        )

        voting_stat.additional_properties = d
        return voting_stat

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
