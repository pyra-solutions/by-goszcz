from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.group_member import GroupMember


T = TypeVar("T", bound="GroupDetails")


@_attrs_define
class GroupDetails:
    """A group details

    Attributes:
        id (int | Unset): ID used to get group details Example: 1.
        name (str | Unset): Name of the group Example: Polsko-Albańska Grupa Parlamentarna.
        eng_name (str | Unset): Name of the group in english Example: Polish-Albanian Parliamentary Group.
        appointment_date (datetime.date | Unset): appointment date Example: 2022-03-10.
        remarks (str | Unset): remarks
        members (list[GroupMember] | Unset): members
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    eng_name: str | Unset = UNSET
    appointment_date: datetime.date | Unset = UNSET
    remarks: str | Unset = UNSET
    members: list[GroupMember] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        eng_name = self.eng_name

        appointment_date: str | Unset = UNSET
        if not isinstance(self.appointment_date, Unset):
            appointment_date = self.appointment_date.isoformat()

        remarks = self.remarks

        members: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.members, Unset):
            members = []
            for members_item_data in self.members:
                members_item = members_item_data.to_dict()
                members.append(members_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if eng_name is not UNSET:
            field_dict["engName"] = eng_name
        if appointment_date is not UNSET:
            field_dict["appointmentDate"] = appointment_date
        if remarks is not UNSET:
            field_dict["remarks"] = remarks
        if members is not UNSET:
            field_dict["members"] = members

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.group_member import GroupMember

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        eng_name = d.pop("engName", UNSET)

        _appointment_date = d.pop("appointmentDate", UNSET)
        appointment_date: datetime.date | Unset
        if isinstance(_appointment_date, Unset):
            appointment_date = UNSET
        else:
            appointment_date = isoparse(_appointment_date).date()

        remarks = d.pop("remarks", UNSET)

        _members = d.pop("members", UNSET)
        members: list[GroupMember] | Unset = UNSET
        if _members is not UNSET:
            members = []
            for members_item_data in _members:
                members_item = GroupMember.from_dict(members_item_data)

                members.append(members_item)

        group_details = cls(
            id=id,
            name=name,
            eng_name=eng_name,
            appointment_date=appointment_date,
            remarks=remarks,
            members=members,
        )

        group_details.additional_properties = d
        return group_details

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
