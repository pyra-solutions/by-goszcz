from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProcessDocument")


@_attrs_define
class ProcessDocument:
    """A document in the legislative process.

    Attributes:
        number (str | Unset): a print number Example: 13-A.
        registered_date (datetime.date | Unset): a date when a document was registered Example: 2019-11-28.
        document_date (datetime.date | Unset): a date of a document Example: 2019-11-28.
        title (str | Unset): a title of a print Example: Opinia Komisji Sprawiedliwości i Praw Człowieka dotycząca
            wniosków w sprawie wyboru na stanowiska sędziów Trybunału Konstytucyjnego..
    """

    number: str | Unset = UNSET
    registered_date: datetime.date | Unset = UNSET
    document_date: datetime.date | Unset = UNSET
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        number = self.number

        registered_date: str | Unset = UNSET
        if not isinstance(self.registered_date, Unset):
            registered_date = self.registered_date.isoformat()

        document_date: str | Unset = UNSET
        if not isinstance(self.document_date, Unset):
            document_date = self.document_date.isoformat()

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if number is not UNSET:
            field_dict["number"] = number
        if registered_date is not UNSET:
            field_dict["registeredDate"] = registered_date
        if document_date is not UNSET:
            field_dict["documentDate"] = document_date
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        number = d.pop("number", UNSET)

        _registered_date = d.pop("registeredDate", UNSET)
        registered_date: datetime.date | Unset
        if isinstance(_registered_date, Unset):
            registered_date = UNSET
        else:
            registered_date = isoparse(_registered_date).date()

        _document_date = d.pop("documentDate", UNSET)
        document_date: datetime.date | Unset
        if isinstance(_document_date, Unset):
            document_date = UNSET
        else:
            document_date = isoparse(_document_date).date()

        title = d.pop("title", UNSET)

        process_document = cls(
            number=number,
            registered_date=registered_date,
            document_date=document_date,
            title=title,
        )

        process_document.additional_properties = d
        return process_document

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
