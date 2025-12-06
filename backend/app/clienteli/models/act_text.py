from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.act_text_type import ActTextType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ActText")


@_attrs_define
class ActText:
    """An information about a text of an act.

    Attributes:
        file_name (str | Unset): a file name Example: D20172196.pdf.
        type_ (ActTextType | Unset): a type of a text Example: O.
    """

    file_name: str | Unset = UNSET
    type_: ActTextType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_name = self.file_name

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file_name = d.pop("fileName", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: ActTextType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ActTextType(_type_)

        act_text = cls(
            file_name=file_name,
            type_=type_,
        )

        act_text.additional_properties = d
        return act_text

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
