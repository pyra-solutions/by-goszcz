from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActInfo")


@_attrs_define
class ActInfo:
    """Basic information about an act.

    Attributes:
        address (str | Unset): an address of publication. An address is in format {publisher}{year}{volume}{position}.
            Example: WDU20170002196.
        publisher (str | Unset): a code of a publisher Example: DU.
        year (int | Unset): a year of publication Example: 2017.
        volume (int | Unset): a volume of a publication. Specifies a volume in year. After year 2012 there are no
            volumes and this field should have value '0'. Example: 1.
        pos (int | Unset): a position in a year (or in a volume before year 2012) Example: 2196.
        title (str | Unset): a title of this act Example: Obwieszczenie Marszałka Sejmu Rzeczypospolitej Polskiej z dnia
            9 listopada 2017 r. w sprawie ogłoszenia jednolitego tekstu ustawy o kształtowaniu ustroju rolnego.
        display_address (str | Unset): a display address Example: Dz.U. 2017 poz. 2332.
        promulgation (datetime.date | Unset): promulgation date Example: 2022-03-10.
        announcement_date (datetime.date | Unset): announcement date Example: 2022-03-10.
        text_pdf (bool | Unset): a flag indicating this act has a PDF text
        text_html (bool | Unset): a flag indicating this act has a HTML text
        change_date (datetime.datetime | Unset): date and time of last change in a document Example: 2018-01-05 12:50.
        eli (str | Unset): an European Legislation Identifier Example: DU/2017/2196.
        type_ (str | Unset): a type of the act Example: Ustawa.
        status (str | Unset): status of the act Example: obowiązujący.
    """

    address: str | Unset = UNSET
    publisher: str | Unset = UNSET
    year: int | Unset = UNSET
    volume: int | Unset = UNSET
    pos: int | Unset = UNSET
    title: str | Unset = UNSET
    display_address: str | Unset = UNSET
    promulgation: datetime.date | Unset = UNSET
    announcement_date: datetime.date | Unset = UNSET
    text_pdf: bool | Unset = UNSET
    text_html: bool | Unset = UNSET
    change_date: datetime.datetime | Unset = UNSET
    eli: str | Unset = UNSET
    type_: str | Unset = UNSET
    status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address = self.address

        publisher = self.publisher

        year = self.year

        volume = self.volume

        pos = self.pos

        title = self.title

        display_address = self.display_address

        promulgation: str | Unset = UNSET
        if not isinstance(self.promulgation, Unset):
            promulgation = self.promulgation.isoformat()

        announcement_date: str | Unset = UNSET
        if not isinstance(self.announcement_date, Unset):
            announcement_date = self.announcement_date.isoformat()

        text_pdf = self.text_pdf

        text_html = self.text_html

        change_date: str | Unset = UNSET
        if not isinstance(self.change_date, Unset):
            change_date = self.change_date.isoformat()

        eli = self.eli

        type_ = self.type_

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if publisher is not UNSET:
            field_dict["publisher"] = publisher
        if year is not UNSET:
            field_dict["year"] = year
        if volume is not UNSET:
            field_dict["volume"] = volume
        if pos is not UNSET:
            field_dict["pos"] = pos
        if title is not UNSET:
            field_dict["title"] = title
        if display_address is not UNSET:
            field_dict["displayAddress"] = display_address
        if promulgation is not UNSET:
            field_dict["promulgation"] = promulgation
        if announcement_date is not UNSET:
            field_dict["announcementDate"] = announcement_date
        if text_pdf is not UNSET:
            field_dict["textPDF"] = text_pdf
        if text_html is not UNSET:
            field_dict["textHTML"] = text_html
        if change_date is not UNSET:
            field_dict["changeDate"] = change_date
        if eli is not UNSET:
            field_dict["ELI"] = eli
        if type_ is not UNSET:
            field_dict["type"] = type_
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        address = d.pop("address", UNSET)

        publisher = d.pop("publisher", UNSET)

        year = d.pop("year", UNSET)

        volume = d.pop("volume", UNSET)

        pos = d.pop("pos", UNSET)

        title = d.pop("title", UNSET)

        display_address = d.pop("displayAddress", UNSET)

        _promulgation = d.pop("promulgation", UNSET)
        promulgation: datetime.date | Unset
        if isinstance(_promulgation, Unset):
            promulgation = UNSET
        else:
            promulgation = isoparse(_promulgation).date()

        _announcement_date = d.pop("announcementDate", UNSET)
        announcement_date: datetime.date | Unset
        if isinstance(_announcement_date, Unset):
            announcement_date = UNSET
        else:
            announcement_date = isoparse(_announcement_date).date()

        text_pdf = d.pop("textPDF", UNSET)

        text_html = d.pop("textHTML", UNSET)

        _change_date = d.pop("changeDate", UNSET)
        change_date: datetime.datetime | Unset
        if isinstance(_change_date, Unset):
            change_date = UNSET
        else:
            change_date = isoparse(_change_date)

        eli = d.pop("ELI", UNSET)

        type_ = d.pop("type", UNSET)

        status = d.pop("status", UNSET)

        act_info = cls(
            address=address,
            publisher=publisher,
            year=year,
            volume=volume,
            pos=pos,
            title=title,
            display_address=display_address,
            promulgation=promulgation,
            announcement_date=announcement_date,
            text_pdf=text_pdf,
            text_html=text_html,
            change_date=change_date,
            eli=eli,
            type_=type_,
            status=status,
        )

        act_info.additional_properties = d
        return act_info

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
