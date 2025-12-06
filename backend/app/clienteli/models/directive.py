from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Directive")


@_attrs_define
class Directive:
    """An European directive.

    Attributes:
        address (str | Unset): an identifier of the directive Example: 32013R0952.
        title (str | Unset): a title of the directive Example: Rozporządzenie Parlamentu Europejskiego i Rady (UE) nr
            952/2013 z dnia 9 października 2013 r. ustanawiające unijny kodeks celny.
        date (datetime.date | Unset): a date of the directive Example: 2013-10-09.
    """

    address: str | Unset = UNSET
    title: str | Unset = UNSET
    date: datetime.date | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address = self.address

        title = self.title

        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if title is not UNSET:
            field_dict["title"] = title
        if date is not UNSET:
            field_dict["date"] = date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        address = d.pop("address", UNSET)

        title = d.pop("title", UNSET)

        _date = d.pop("date", UNSET)
        date: datetime.date | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()

        directive = cls(
            address=address,
            title=title,
            date=date,
        )

        directive.additional_properties = d
        return directive

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
