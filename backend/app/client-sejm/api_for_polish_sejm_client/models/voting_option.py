from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="VotingOption")


@_attrs_define
class VotingOption:
    """voting option when voting on a list

    Attributes:
        option_index (int | Unset): an option index Example: 1.
        option (str | Unset): an option Example: STAROŃ LIDIA, INFORMACJA NR 1.
        description (str | Unset): an optional description Example: w sprawie realizacji rządowego "Programu budowy 100
            obwodnic na lata 2020-2030".
        votes (int | Unset): number of votes for this option Example: 213.
    """

    option_index: int | Unset = UNSET
    option: str | Unset = UNSET
    description: str | Unset = UNSET
    votes: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        option_index = self.option_index

        option = self.option

        description = self.description

        votes = self.votes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if option_index is not UNSET:
            field_dict["optionIndex"] = option_index
        if option is not UNSET:
            field_dict["option"] = option
        if description is not UNSET:
            field_dict["description"] = description
        if votes is not UNSET:
            field_dict["votes"] = votes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        option_index = d.pop("optionIndex", UNSET)

        option = d.pop("option", UNSET)

        description = d.pop("description", UNSET)

        votes = d.pop("votes", UNSET)

        voting_option = cls(
            option_index=option_index,
            option=option,
            description=description,
            votes=votes,
        )

        voting_option.additional_properties = d
        return voting_option

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
