from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PrintInfo")


@_attrs_define
class PrintInfo:
    """info about prints

    Attributes:
        count (int | Unset): number of prints Example: 735.
        last_changed (datetime.datetime | Unset): date of last changed document Example: 2022-03-10 12:15:50.
        link (str | Unset): a link to prints endpoint
    """

    count: int | Unset = UNSET
    last_changed: datetime.datetime | Unset = UNSET
    link: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        last_changed: str | Unset = UNSET
        if not isinstance(self.last_changed, Unset):
            last_changed = self.last_changed.isoformat()

        link = self.link

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if last_changed is not UNSET:
            field_dict["lastChanged"] = last_changed
        if link is not UNSET:
            field_dict["link"] = link

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        count = d.pop("count", UNSET)

        _last_changed = d.pop("lastChanged", UNSET)
        last_changed: datetime.datetime | Unset
        if isinstance(_last_changed, Unset):
            last_changed = UNSET
        else:
            last_changed = isoparse(_last_changed)

        link = d.pop("link", UNSET)

        print_info = cls(
            count=count,
            last_changed=last_changed,
            link=link,
        )

        print_info.additional_properties = d
        return print_info

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
