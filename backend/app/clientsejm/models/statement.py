from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Statement")


@_attrs_define
class Statement:
    """statement on a sitting

    Attributes:
        num (int | Unset): statement number, 0 is always for course of the sitting Example: 15.
        function (str | Unset): function of the speaker Example: Minister Rozwoju i Technologii.
        name (str | Unset): name of the speaker Example: Jan Kowalski.
        member_id (int | Unset): MP id number, if speaker is an MP, 0 otherwise Example: 35.
        rapporteur (bool | Unset): this statement was made by the rapporteur
        secretary (bool | Unset): this statement was made by the secretary
        start_date_time (datetime.datetime | Unset): start time of the statement Example: 2022-03-10 12:15:50.
        end_date_time (datetime.datetime | Unset): end time of the statement Example: 2022-03-10 12:15:50.
        unspoken (bool | Unset): is this is unspoken statement
    """

    num: int | Unset = UNSET
    function: str | Unset = UNSET
    name: str | Unset = UNSET
    member_id: int | Unset = UNSET
    rapporteur: bool | Unset = UNSET
    secretary: bool | Unset = UNSET
    start_date_time: datetime.datetime | Unset = UNSET
    end_date_time: datetime.datetime | Unset = UNSET
    unspoken: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        num = self.num

        function = self.function

        name = self.name

        member_id = self.member_id

        rapporteur = self.rapporteur

        secretary = self.secretary

        start_date_time: str | Unset = UNSET
        if not isinstance(self.start_date_time, Unset):
            start_date_time = self.start_date_time.isoformat()

        end_date_time: str | Unset = UNSET
        if not isinstance(self.end_date_time, Unset):
            end_date_time = self.end_date_time.isoformat()

        unspoken = self.unspoken

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if num is not UNSET:
            field_dict["num"] = num
        if function is not UNSET:
            field_dict["function"] = function
        if name is not UNSET:
            field_dict["name"] = name
        if member_id is not UNSET:
            field_dict["memberID"] = member_id
        if rapporteur is not UNSET:
            field_dict["rapporteur"] = rapporteur
        if secretary is not UNSET:
            field_dict["secretary"] = secretary
        if start_date_time is not UNSET:
            field_dict["startDateTime"] = start_date_time
        if end_date_time is not UNSET:
            field_dict["endDateTime"] = end_date_time
        if unspoken is not UNSET:
            field_dict["unspoken"] = unspoken

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        num = d.pop("num", UNSET)

        function = d.pop("function", UNSET)

        name = d.pop("name", UNSET)

        member_id = d.pop("memberID", UNSET)

        rapporteur = d.pop("rapporteur", UNSET)

        secretary = d.pop("secretary", UNSET)

        _start_date_time = d.pop("startDateTime", UNSET)
        start_date_time: datetime.datetime | Unset
        if isinstance(_start_date_time, Unset):
            start_date_time = UNSET
        else:
            start_date_time = isoparse(_start_date_time)

        _end_date_time = d.pop("endDateTime", UNSET)
        end_date_time: datetime.datetime | Unset
        if isinstance(_end_date_time, Unset):
            end_date_time = UNSET
        else:
            end_date_time = isoparse(_end_date_time)

        unspoken = d.pop("unspoken", UNSET)

        statement = cls(
            num=num,
            function=function,
            name=name,
            member_id=member_id,
            rapporteur=rapporteur,
            secretary=secretary,
            start_date_time=start_date_time,
            end_date_time=end_date_time,
            unspoken=unspoken,
        )

        statement.additional_properties = d
        return statement

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
