from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.member_type import MemberType
from ..types import UNSET, Unset

T = TypeVar("T", bound="GroupMember")


@_attrs_define
class GroupMember:
    """Information about a member of a group

    Attributes:
        id (str | Unset): A number of the identity card of the MP Example: 6.
        name (str | Unset): Last and first name of the MP Example: Andzel Waldemar.
        club (str | Unset): Name of a club Example: PiS.
        senator (bool | Unset): A flag indicating that a member is not an MP, but a senate member
        type_ (MemberType | Unset):
        membership_start (datetime.date | Unset): A date when membership in this group started Example: 2023-10-10.
        membership_end (datetime.date | Unset): A date when membership in this group ended Example: 2023-10-10.
        mandate_end (datetime.date | Unset): A date when mandate of MP expired Example: 2023-10-10.
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    club: str | Unset = UNSET
    senator: bool | Unset = UNSET
    type_: MemberType | Unset = UNSET
    membership_start: datetime.date | Unset = UNSET
    membership_end: datetime.date | Unset = UNSET
    mandate_end: datetime.date | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        club = self.club

        senator = self.senator

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        membership_start: str | Unset = UNSET
        if not isinstance(self.membership_start, Unset):
            membership_start = self.membership_start.isoformat()

        membership_end: str | Unset = UNSET
        if not isinstance(self.membership_end, Unset):
            membership_end = self.membership_end.isoformat()

        mandate_end: str | Unset = UNSET
        if not isinstance(self.mandate_end, Unset):
            mandate_end = self.mandate_end.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if club is not UNSET:
            field_dict["club"] = club
        if senator is not UNSET:
            field_dict["senator"] = senator
        if type_ is not UNSET:
            field_dict["type"] = type_
        if membership_start is not UNSET:
            field_dict["membershipStart"] = membership_start
        if membership_end is not UNSET:
            field_dict["membershipEnd"] = membership_end
        if mandate_end is not UNSET:
            field_dict["mandateEnd"] = mandate_end

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        club = d.pop("club", UNSET)

        senator = d.pop("senator", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: MemberType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = MemberType(_type_)

        _membership_start = d.pop("membershipStart", UNSET)
        membership_start: datetime.date | Unset
        if isinstance(_membership_start, Unset):
            membership_start = UNSET
        else:
            membership_start = isoparse(_membership_start).date()

        _membership_end = d.pop("membershipEnd", UNSET)
        membership_end: datetime.date | Unset
        if isinstance(_membership_end, Unset):
            membership_end = UNSET
        else:
            membership_end = isoparse(_membership_end).date()

        _mandate_end = d.pop("mandateEnd", UNSET)
        mandate_end: datetime.date | Unset
        if isinstance(_mandate_end, Unset):
            mandate_end = UNSET
        else:
            mandate_end = isoparse(_mandate_end).date()

        group_member = cls(
            id=id,
            name=name,
            club=club,
            senator=senator,
            type_=type_,
            membership_start=membership_start,
            membership_end=membership_end,
            mandate_end=mandate_end,
        )

        group_member.additional_properties = d
        return group_member

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
