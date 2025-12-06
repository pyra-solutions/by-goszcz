from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.act_info import ActInfo


T = TypeVar("T", bound="ReferenceDetailsInfo")


@_attrs_define
class ReferenceDetailsInfo:
    """information about a reference (with act header)

    Attributes:
        act (ActInfo | Unset): Basic information about an act.
        art (str | Unset): referenced article (optional) Example: art. 30a ust. 5.
        date (datetime.date | Unset): a date (optional, e.g. for repeal) Example: 2017-01-05.
    """

    act: ActInfo | Unset = UNSET
    art: str | Unset = UNSET
    date: datetime.date | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        act: dict[str, Any] | Unset = UNSET
        if not isinstance(self.act, Unset):
            act = self.act.to_dict()

        art = self.art

        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if act is not UNSET:
            field_dict["act"] = act
        if art is not UNSET:
            field_dict["art"] = art
        if date is not UNSET:
            field_dict["date"] = date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.act_info import ActInfo

        d = dict(src_dict)
        _act = d.pop("act", UNSET)
        act: ActInfo | Unset
        if isinstance(_act, Unset):
            act = UNSET
        else:
            act = ActInfo.from_dict(_act)

        art = d.pop("art", UNSET)

        _date = d.pop("date", UNSET)
        date: datetime.date | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()

        reference_details_info = cls(
            act=act,
            art=art,
            date=date,
        )

        reference_details_info.additional_properties = d
        return reference_details_info

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
