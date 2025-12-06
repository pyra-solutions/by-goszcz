from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sort_column import SortColumn
from ..models.sort_dir import SortDir
from ..types import UNSET, Unset

T = TypeVar("T", bound="ActOrder")


@_attrs_define
class ActOrder:
    """a sorting order

    Attributes:
        column (SortColumn | Unset):
        dir_ (SortDir | Unset):
    """

    column: SortColumn | Unset = UNSET
    dir_: SortDir | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        column: str | Unset = UNSET
        if not isinstance(self.column, Unset):
            column = self.column.value

        dir_: str | Unset = UNSET
        if not isinstance(self.dir_, Unset):
            dir_ = self.dir_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if column is not UNSET:
            field_dict["column"] = column
        if dir_ is not UNSET:
            field_dict["dir"] = dir_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _column = d.pop("column", UNSET)
        column: SortColumn | Unset
        if isinstance(_column, Unset):
            column = UNSET
        else:
            column = SortColumn(_column)

        _dir_ = d.pop("dir", UNSET)
        dir_: SortDir | Unset
        if isinstance(_dir_, Unset):
            dir_ = UNSET
        else:
            dir_ = SortDir(_dir_)

        act_order = cls(
            column=column,
            dir_=dir_,
        )

        act_order.additional_properties = d
        return act_order

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
