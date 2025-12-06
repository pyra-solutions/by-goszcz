from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PrintRef")


@_attrs_define
class PrintRef:
    """An information about a print and legislative process.

    Attributes:
        term (int | Unset): a term of Sejm when this print was published Example: 8.
        number (str | Unset): a number of the print Example: 1407.
        link (str | Unset): a link to details of a legislative process Example:
            https://www.sejm.gov.pl/Sejm8.nsf/PrzebiegProc.xsp?nr=1407.
        link_print_api (str | Unset): a link to API for print details Example:
            https://api.sejm.gov.pl/sejm/term8/prints/1407.
        link_process_api (str | Unset): a link to API for process details Example:
            https://api.sejm.gov.pl/sejm/term8/processes/1407.
    """

    term: int | Unset = UNSET
    number: str | Unset = UNSET
    link: str | Unset = UNSET
    link_print_api: str | Unset = UNSET
    link_process_api: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        term = self.term

        number = self.number

        link = self.link

        link_print_api = self.link_print_api

        link_process_api = self.link_process_api

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if term is not UNSET:
            field_dict["term"] = term
        if number is not UNSET:
            field_dict["number"] = number
        if link is not UNSET:
            field_dict["link"] = link
        if link_print_api is not UNSET:
            field_dict["linkPrintAPI"] = link_print_api
        if link_process_api is not UNSET:
            field_dict["linkProcessAPI"] = link_process_api

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        term = d.pop("term", UNSET)

        number = d.pop("number", UNSET)

        link = d.pop("link", UNSET)

        link_print_api = d.pop("linkPrintAPI", UNSET)

        link_process_api = d.pop("linkProcessAPI", UNSET)

        print_ref = cls(
            term=term,
            number=number,
            link=link,
            link_print_api=link_print_api,
            link_process_api=link_process_api,
        )

        print_ref.additional_properties = d
        return print_ref

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
