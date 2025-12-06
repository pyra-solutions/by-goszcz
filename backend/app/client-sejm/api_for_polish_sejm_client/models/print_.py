from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Print")


@_attrs_define
class Print:
    """A print

    Attributes:
        term (int | Unset): a Sejm term Example: 9.
        number (str | Unset): a number of a print in the specified Sejm term Example: 19, 1006-A.
        number_associated (list[str] | Unset): numbers of prints that this print is associated with Example: 609.
        title (str | Unset): a title of a print Example: Opinia Komisji Sprawiedliwości i Praw Człowieka dotycząca
            wniosków w sprawie wyboru na stanowiska sędziów Trybunału Konstytucyjnego..
        document_date (datetime.date | Unset): a date of a print Example: 2019-11-20.
        delivery_date (datetime.date | Unset): a date of delivery of a print Example: 2019-11-20.
        process_print (list[str] | Unset): a list of prints that started a legislative process that this print is
            connected to Example: ['16', '17'].
        change_date (datetime.datetime | Unset): a date of of last change to the print Example: 2020-10-02 12:49:35.
        attachments (list[str] | Unset): a list of attachments added to the print
        additional_prints (list[Print] | Unset): a list of additional prints added to the print
    """

    term: int | Unset = UNSET
    number: str | Unset = UNSET
    number_associated: list[str] | Unset = UNSET
    title: str | Unset = UNSET
    document_date: datetime.date | Unset = UNSET
    delivery_date: datetime.date | Unset = UNSET
    process_print: list[str] | Unset = UNSET
    change_date: datetime.datetime | Unset = UNSET
    attachments: list[str] | Unset = UNSET
    additional_prints: list[Print] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        term = self.term

        number = self.number

        number_associated: list[str] | Unset = UNSET
        if not isinstance(self.number_associated, Unset):
            number_associated = self.number_associated

        title = self.title

        document_date: str | Unset = UNSET
        if not isinstance(self.document_date, Unset):
            document_date = self.document_date.isoformat()

        delivery_date: str | Unset = UNSET
        if not isinstance(self.delivery_date, Unset):
            delivery_date = self.delivery_date.isoformat()

        process_print: list[str] | Unset = UNSET
        if not isinstance(self.process_print, Unset):
            process_print = self.process_print

        change_date: str | Unset = UNSET
        if not isinstance(self.change_date, Unset):
            change_date = self.change_date.isoformat()

        attachments: list[str] | Unset = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = self.attachments

        additional_prints: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.additional_prints, Unset):
            additional_prints = []
            for additional_prints_item_data in self.additional_prints:
                additional_prints_item = additional_prints_item_data.to_dict()
                additional_prints.append(additional_prints_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if term is not UNSET:
            field_dict["term"] = term
        if number is not UNSET:
            field_dict["number"] = number
        if number_associated is not UNSET:
            field_dict["numberAssociated"] = number_associated
        if title is not UNSET:
            field_dict["title"] = title
        if document_date is not UNSET:
            field_dict["documentDate"] = document_date
        if delivery_date is not UNSET:
            field_dict["deliveryDate"] = delivery_date
        if process_print is not UNSET:
            field_dict["processPrint"] = process_print
        if change_date is not UNSET:
            field_dict["changeDate"] = change_date
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if additional_prints is not UNSET:
            field_dict["additionalPrints"] = additional_prints

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        term = d.pop("term", UNSET)

        number = d.pop("number", UNSET)

        number_associated = cast(list[str], d.pop("numberAssociated", UNSET))

        title = d.pop("title", UNSET)

        _document_date = d.pop("documentDate", UNSET)
        document_date: datetime.date | Unset
        if isinstance(_document_date, Unset):
            document_date = UNSET
        else:
            document_date = isoparse(_document_date).date()

        _delivery_date = d.pop("deliveryDate", UNSET)
        delivery_date: datetime.date | Unset
        if isinstance(_delivery_date, Unset):
            delivery_date = UNSET
        else:
            delivery_date = isoparse(_delivery_date).date()

        process_print = cast(list[str], d.pop("processPrint", UNSET))

        _change_date = d.pop("changeDate", UNSET)
        change_date: datetime.datetime | Unset
        if isinstance(_change_date, Unset):
            change_date = UNSET
        else:
            change_date = isoparse(_change_date)

        attachments = cast(list[str], d.pop("attachments", UNSET))

        _additional_prints = d.pop("additionalPrints", UNSET)
        additional_prints: list[Print] | Unset = UNSET
        if _additional_prints is not UNSET:
            additional_prints = []
            for additional_prints_item_data in _additional_prints:
                additional_prints_item = Print.from_dict(additional_prints_item_data)

                additional_prints.append(additional_prints_item)

        print_ = cls(
            term=term,
            number=number,
            number_associated=number_associated,
            title=title,
            document_date=document_date,
            delivery_date=delivery_date,
            process_print=process_print,
            change_date=change_date,
            attachments=attachments,
            additional_prints=additional_prints,
        )

        print_.additional_properties = d
        return print_

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
