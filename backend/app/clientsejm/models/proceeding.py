from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Proceeding")


@_attrs_define
class Proceeding:
    """A proceeding.

    Attributes:
        title (str | Unset): a title of the proceeding Example: 1. Posiedzenie Sejmu RP w dniach 12, 13, 19 i 21
            listopada 2019 r..
        dates (list[datetime.date] | Unset): a dates of the proceeding
        current (bool | Unset): is this a current proceeding
        agenda (str | Unset): agenda of a proceeding
        schedule (str | Unset): schedule of a proceeding (only for current proceeding)
        votings (str | Unset): schedule of votings for a proceeding (only for current proceeding)
        current_affairs (str | Unset): current information and questions on current affairs (only for current
            proceeding)
        number (int | Unset): a proceeding number Example: 1.
    """

    title: str | Unset = UNSET
    dates: list[datetime.date] | Unset = UNSET
    current: bool | Unset = UNSET
    agenda: str | Unset = UNSET
    schedule: str | Unset = UNSET
    votings: str | Unset = UNSET
    current_affairs: str | Unset = UNSET
    number: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        dates: list[str] | Unset = UNSET
        if not isinstance(self.dates, Unset):
            dates = []
            for dates_item_data in self.dates:
                dates_item = dates_item_data.isoformat()
                dates.append(dates_item)

        current = self.current

        agenda = self.agenda

        schedule = self.schedule

        votings = self.votings

        current_affairs = self.current_affairs

        number = self.number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if dates is not UNSET:
            field_dict["dates"] = dates
        if current is not UNSET:
            field_dict["current"] = current
        if agenda is not UNSET:
            field_dict["agenda"] = agenda
        if schedule is not UNSET:
            field_dict["schedule"] = schedule
        if votings is not UNSET:
            field_dict["votings"] = votings
        if current_affairs is not UNSET:
            field_dict["currentAffairs"] = current_affairs
        if number is not UNSET:
            field_dict["number"] = number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title", UNSET)

        _dates = d.pop("dates", UNSET)
        dates: list[datetime.date] | Unset = UNSET
        if _dates is not UNSET:
            dates = []
            for dates_item_data in _dates:
                dates_item = isoparse(dates_item_data).date()

                dates.append(dates_item)

        current = d.pop("current", UNSET)

        agenda = d.pop("agenda", UNSET)

        schedule = d.pop("schedule", UNSET)

        votings = d.pop("votings", UNSET)

        current_affairs = d.pop("currentAffairs", UNSET)

        number = d.pop("number", UNSET)

        proceeding = cls(
            title=title,
            dates=dates,
            current=current,
            agenda=agenda,
            schedule=schedule,
            votings=votings,
            current_affairs=current_affairs,
            number=number,
        )

        proceeding.additional_properties = d
        return proceeding

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
