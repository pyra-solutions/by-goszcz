from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActReference")


@_attrs_define
class ActReference:
    """A reference from one act to another act.

    Attributes:
        article (str | Unset): referenced article (optional) Example: art. 30a ust. 5.
        date (datetime.date | Unset): a date (optional, e.g. for repeal) Example: 2017-01-05.
        change_date (datetime.datetime | Unset): date and time of last change in a document Example: 2018-01-05 12:50.
        act (str | Unset): a referenced act
        type_ (str | Unset): a type of reference Example: Akty zmieniające.
    """

    article: str | Unset = UNSET
    date: datetime.date | Unset = UNSET
    change_date: datetime.datetime | Unset = UNSET
    act: str | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        article = self.article

        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        change_date: str | Unset = UNSET
        if not isinstance(self.change_date, Unset):
            change_date = self.change_date.isoformat()

        act = self.act

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if article is not UNSET:
            field_dict["article"] = article
        if date is not UNSET:
            field_dict["date"] = date
        if change_date is not UNSET:
            field_dict["changeDate"] = change_date
        if act is not UNSET:
            field_dict["act"] = act
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        article = d.pop("article", UNSET)

        _date = d.pop("date", UNSET)
        date: datetime.date | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()

        _change_date = d.pop("changeDate", UNSET)
        change_date: datetime.datetime | Unset
        if isinstance(_change_date, Unset):
            change_date = UNSET
        else:
            change_date = isoparse(_change_date)

        act = d.pop("act", UNSET)

        type_ = d.pop("type", UNSET)

        act_reference = cls(
            article=article,
            date=date,
            change_date=change_date,
            act=act,
            type_=type_,
        )

        act_reference.additional_properties = d
        return act_reference

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
