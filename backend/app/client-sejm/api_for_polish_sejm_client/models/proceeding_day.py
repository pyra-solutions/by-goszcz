from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProceedingDay")


@_attrs_define
class ProceedingDay:
    """info about a proceeding day

    Attributes:
        proceeding (int | Unset): proceeding number
        date (datetime.date | Unset): proceeding date Example: 2022-03-10.
        votings_num (int | Unset): number of votings on this day
    """

    proceeding: int | Unset = UNSET
    date: datetime.date | Unset = UNSET
    votings_num: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        proceeding = self.proceeding

        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        votings_num = self.votings_num

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if proceeding is not UNSET:
            field_dict["proceeding"] = proceeding
        if date is not UNSET:
            field_dict["date"] = date
        if votings_num is not UNSET:
            field_dict["votingsNum"] = votings_num

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        proceeding = d.pop("proceeding", UNSET)

        _date = d.pop("date", UNSET)
        date: datetime.date | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()

        votings_num = d.pop("votingsNum", UNSET)

        proceeding_day = cls(
            proceeding=proceeding,
            date=date,
            votings_num=votings_num,
        )

        proceeding_day.additional_properties = d
        return proceeding_day

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
