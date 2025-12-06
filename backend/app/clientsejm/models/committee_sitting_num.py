from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CommitteeSittingNum")


@_attrs_define
class CommitteeSittingNum:
    """A sitting code and number

    Attributes:
        num (int | Unset): A sitting number Example: 1.
        code (str | Unset): A committee code Example: ASW.
    """

    num: int | Unset = UNSET
    code: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        num = self.num

        code = self.code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if num is not UNSET:
            field_dict["num"] = num
        if code is not UNSET:
            field_dict["code"] = code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        num = d.pop("num", UNSET)

        code = d.pop("code", UNSET)

        committee_sitting_num = cls(
            num=num,
            code=code,
        )

        committee_sitting_num.additional_properties = d
        return committee_sitting_num

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
