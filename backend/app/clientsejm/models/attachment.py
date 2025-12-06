from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Attachment")


@_attrs_define
class Attachment:
    """An attachment.

    Attributes:
        last_modified (datetime.datetime | Unset): A date of last modification of a document Example: 2022-09-07
            15:01:42.
        name (str | Unset): A name of the file Example: i14710-o3.pdf.
        url (str | Unset): An url to download a file Example:
            https://orka2.sejm.gov.pl/INT9.nsf/klucz/ATTBXWKH2/$FILE/i14710-o3.pdf.
    """

    last_modified: datetime.datetime | Unset = UNSET
    name: str | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        last_modified: str | Unset = UNSET
        if not isinstance(self.last_modified, Unset):
            last_modified = self.last_modified.isoformat()

        name = self.name

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if last_modified is not UNSET:
            field_dict["lastModified"] = last_modified
        if name is not UNSET:
            field_dict["name"] = name
        if url is not UNSET:
            field_dict["URL"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _last_modified = d.pop("lastModified", UNSET)
        last_modified: datetime.datetime | Unset
        if isinstance(_last_modified, Unset):
            last_modified = UNSET
        else:
            last_modified = isoparse(_last_modified)

        name = d.pop("name", UNSET)

        url = d.pop("URL", UNSET)

        attachment = cls(
            last_modified=last_modified,
            name=name,
            url=url,
        )

        attachment.additional_properties = d
        return attachment

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
