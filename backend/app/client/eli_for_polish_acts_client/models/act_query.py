from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.search_date import SearchDate
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.act_order import ActOrder


T = TypeVar("T", bound="ActQuery")


@_attrs_define
class ActQuery:
    """a query for searching acts

    Attributes:
        exile (bool | Unset): include acts from Polish authorities in exile
        status_in_force (bool | Unset): include only acts in force
        publisher (str | Unset): a code of the selected publisher
        publisher_name (str | Unset): a name of the selected publisher
        year (int | Unset): a selected year of publication
        volume (int | Unset): a selected volume of publication
        position (int | Unset): a selected position of publication
        title (str | Unset): a title to search for
        type_ (list[str] | Unset): a list of act types to search for
        keyword (list[str] | Unset): a list of keywords to search for
        date_type (SearchDate | Unset):
        date_from (datetime.date | Unset): a date of announcement to search from Example: 2022-03-10.
        date_to (datetime.date | Unset): a date of announcement to search to Example: 2022-03-10.
        date_effect_type (SearchDate | Unset):
        date_effect_from (datetime.date | Unset): a date of effect to search from Example: 2022-03-10.
        date_effect_to (datetime.date | Unset): a date of effect to search to Example: 2022-03-10.
        pub_date_type (SearchDate | Unset):
        pub_date_from (datetime.date | Unset): a date of publication to search from Example: 2022-03-10.
        pub_date_to (datetime.date | Unset): a date of publication to search to Example: 2022-03-10.
        comparator (ActOrder | Unset): a sorting order
    """

    exile: bool | Unset = UNSET
    status_in_force: bool | Unset = UNSET
    publisher: str | Unset = UNSET
    publisher_name: str | Unset = UNSET
    year: int | Unset = UNSET
    volume: int | Unset = UNSET
    position: int | Unset = UNSET
    title: str | Unset = UNSET
    type_: list[str] | Unset = UNSET
    keyword: list[str] | Unset = UNSET
    date_type: SearchDate | Unset = UNSET
    date_from: datetime.date | Unset = UNSET
    date_to: datetime.date | Unset = UNSET
    date_effect_type: SearchDate | Unset = UNSET
    date_effect_from: datetime.date | Unset = UNSET
    date_effect_to: datetime.date | Unset = UNSET
    pub_date_type: SearchDate | Unset = UNSET
    pub_date_from: datetime.date | Unset = UNSET
    pub_date_to: datetime.date | Unset = UNSET
    comparator: ActOrder | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exile = self.exile

        status_in_force = self.status_in_force

        publisher = self.publisher

        publisher_name = self.publisher_name

        year = self.year

        volume = self.volume

        position = self.position

        title = self.title

        type_: list[str] | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_

        keyword: list[str] | Unset = UNSET
        if not isinstance(self.keyword, Unset):
            keyword = self.keyword

        date_type: str | Unset = UNSET
        if not isinstance(self.date_type, Unset):
            date_type = self.date_type.value

        date_from: str | Unset = UNSET
        if not isinstance(self.date_from, Unset):
            date_from = self.date_from.isoformat()

        date_to: str | Unset = UNSET
        if not isinstance(self.date_to, Unset):
            date_to = self.date_to.isoformat()

        date_effect_type: str | Unset = UNSET
        if not isinstance(self.date_effect_type, Unset):
            date_effect_type = self.date_effect_type.value

        date_effect_from: str | Unset = UNSET
        if not isinstance(self.date_effect_from, Unset):
            date_effect_from = self.date_effect_from.isoformat()

        date_effect_to: str | Unset = UNSET
        if not isinstance(self.date_effect_to, Unset):
            date_effect_to = self.date_effect_to.isoformat()

        pub_date_type: str | Unset = UNSET
        if not isinstance(self.pub_date_type, Unset):
            pub_date_type = self.pub_date_type.value

        pub_date_from: str | Unset = UNSET
        if not isinstance(self.pub_date_from, Unset):
            pub_date_from = self.pub_date_from.isoformat()

        pub_date_to: str | Unset = UNSET
        if not isinstance(self.pub_date_to, Unset):
            pub_date_to = self.pub_date_to.isoformat()

        comparator: dict[str, Any] | Unset = UNSET
        if not isinstance(self.comparator, Unset):
            comparator = self.comparator.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if exile is not UNSET:
            field_dict["exile"] = exile
        if status_in_force is not UNSET:
            field_dict["statusInForce"] = status_in_force
        if publisher is not UNSET:
            field_dict["publisher"] = publisher
        if publisher_name is not UNSET:
            field_dict["publisherName"] = publisher_name
        if year is not UNSET:
            field_dict["year"] = year
        if volume is not UNSET:
            field_dict["volume"] = volume
        if position is not UNSET:
            field_dict["position"] = position
        if title is not UNSET:
            field_dict["title"] = title
        if type_ is not UNSET:
            field_dict["type"] = type_
        if keyword is not UNSET:
            field_dict["keyword"] = keyword
        if date_type is not UNSET:
            field_dict["dateType"] = date_type
        if date_from is not UNSET:
            field_dict["dateFrom"] = date_from
        if date_to is not UNSET:
            field_dict["dateTo"] = date_to
        if date_effect_type is not UNSET:
            field_dict["dateEffectType"] = date_effect_type
        if date_effect_from is not UNSET:
            field_dict["dateEffectFrom"] = date_effect_from
        if date_effect_to is not UNSET:
            field_dict["dateEffectTo"] = date_effect_to
        if pub_date_type is not UNSET:
            field_dict["pubDateType"] = pub_date_type
        if pub_date_from is not UNSET:
            field_dict["pubDateFrom"] = pub_date_from
        if pub_date_to is not UNSET:
            field_dict["pubDateTo"] = pub_date_to
        if comparator is not UNSET:
            field_dict["comparator"] = comparator

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.act_order import ActOrder

        d = dict(src_dict)
        exile = d.pop("exile", UNSET)

        status_in_force = d.pop("statusInForce", UNSET)

        publisher = d.pop("publisher", UNSET)

        publisher_name = d.pop("publisherName", UNSET)

        year = d.pop("year", UNSET)

        volume = d.pop("volume", UNSET)

        position = d.pop("position", UNSET)

        title = d.pop("title", UNSET)

        type_ = cast(list[str], d.pop("type", UNSET))

        keyword = cast(list[str], d.pop("keyword", UNSET))

        _date_type = d.pop("dateType", UNSET)
        date_type: SearchDate | Unset
        if isinstance(_date_type, Unset):
            date_type = UNSET
        else:
            date_type = SearchDate(_date_type)

        _date_from = d.pop("dateFrom", UNSET)
        date_from: datetime.date | Unset
        if isinstance(_date_from, Unset):
            date_from = UNSET
        else:
            date_from = isoparse(_date_from).date()

        _date_to = d.pop("dateTo", UNSET)
        date_to: datetime.date | Unset
        if isinstance(_date_to, Unset):
            date_to = UNSET
        else:
            date_to = isoparse(_date_to).date()

        _date_effect_type = d.pop("dateEffectType", UNSET)
        date_effect_type: SearchDate | Unset
        if isinstance(_date_effect_type, Unset):
            date_effect_type = UNSET
        else:
            date_effect_type = SearchDate(_date_effect_type)

        _date_effect_from = d.pop("dateEffectFrom", UNSET)
        date_effect_from: datetime.date | Unset
        if isinstance(_date_effect_from, Unset):
            date_effect_from = UNSET
        else:
            date_effect_from = isoparse(_date_effect_from).date()

        _date_effect_to = d.pop("dateEffectTo", UNSET)
        date_effect_to: datetime.date | Unset
        if isinstance(_date_effect_to, Unset):
            date_effect_to = UNSET
        else:
            date_effect_to = isoparse(_date_effect_to).date()

        _pub_date_type = d.pop("pubDateType", UNSET)
        pub_date_type: SearchDate | Unset
        if isinstance(_pub_date_type, Unset):
            pub_date_type = UNSET
        else:
            pub_date_type = SearchDate(_pub_date_type)

        _pub_date_from = d.pop("pubDateFrom", UNSET)
        pub_date_from: datetime.date | Unset
        if isinstance(_pub_date_from, Unset):
            pub_date_from = UNSET
        else:
            pub_date_from = isoparse(_pub_date_from).date()

        _pub_date_to = d.pop("pubDateTo", UNSET)
        pub_date_to: datetime.date | Unset
        if isinstance(_pub_date_to, Unset):
            pub_date_to = UNSET
        else:
            pub_date_to = isoparse(_pub_date_to).date()

        _comparator = d.pop("comparator", UNSET)
        comparator: ActOrder | Unset
        if isinstance(_comparator, Unset):
            comparator = UNSET
        else:
            comparator = ActOrder.from_dict(_comparator)

        act_query = cls(
            exile=exile,
            status_in_force=status_in_force,
            publisher=publisher,
            publisher_name=publisher_name,
            year=year,
            volume=volume,
            position=position,
            title=title,
            type_=type_,
            keyword=keyword,
            date_type=date_type,
            date_from=date_from,
            date_to=date_to,
            date_effect_type=date_effect_type,
            date_effect_from=date_effect_from,
            date_effect_to=date_effect_to,
            pub_date_type=pub_date_type,
            pub_date_from=pub_date_from,
            pub_date_to=pub_date_to,
            comparator=comparator,
        )

        act_query.additional_properties = d
        return act_query

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
