from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PublishingHouse")


@_attrs_define
class PublishingHouse:
    """An information about a publisher.

    Attributes:
        code (str | Unset): a unique code of a publisher Example: DU.
        short_name (str | Unset): a short name used to designate an act Example: Dz. U..
        name (str | Unset): a full name of the publisher Example: Dziennik Ustaw.
        acts_count (int | Unset): count of acts Example: 123.
        years (list[int] | Unset): a list of years for which there are acts Example: [1990, 1991, 1992].
    """

    code: str | Unset = UNSET
    short_name: str | Unset = UNSET
    name: str | Unset = UNSET
    acts_count: int | Unset = UNSET
    years: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        short_name = self.short_name

        name = self.name

        acts_count = self.acts_count

        years: list[int] | Unset = UNSET
        if not isinstance(self.years, Unset):
            years = self.years

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if short_name is not UNSET:
            field_dict["shortName"] = short_name
        if name is not UNSET:
            field_dict["name"] = name
        if acts_count is not UNSET:
            field_dict["actsCount"] = acts_count
        if years is not UNSET:
            field_dict["years"] = years

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code", UNSET)

        short_name = d.pop("shortName", UNSET)

        name = d.pop("name", UNSET)

        acts_count = d.pop("actsCount", UNSET)

        years = cast(list[int], d.pop("years", UNSET))

        publishing_house = cls(
            code=code,
            short_name=short_name,
            name=name,
            acts_count=acts_count,
            years=years,
        )

        publishing_house.additional_properties = d
        return publishing_house

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
