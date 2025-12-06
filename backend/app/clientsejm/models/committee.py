from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.comittee_type import ComitteeType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.member import Member


T = TypeVar("T", bound="Committee")


@_attrs_define
class Committee:
    """A comittee.

    Attributes:
        code (str | Unset): Code of committee Example: ENM.
        name (str | Unset): Name of the committee Example: Komisja Edukacji, Nauki i Młodzieży.
        name_genitive (str | Unset): Name of the committee in genitive Example: Komisji Edukacji, Nauki i Młodzieży.
        type_ (ComitteeType | Unset):
        phone (str | Unset): Phone of the committee Example: (22) 694-12-99, 694-20-85.
        appointment_date (datetime.date | Unset): Date of appointment Example: 2019-11-13.
        composition_date (datetime.date | Unset): Date of composition Example: 2019-11-13.
        scope (str | Unset): Description of the committee Example: Do zakresu działania Komisji należą sprawy
            kształcenia i wychowania przedszkolnego, podstawowego, ogólnokształcącego, zawodowego, pomaturalnego i wyższego,
            ....
        members (list[Member] | Unset): a list of committee members (current or at the date of closing the committee)
        sub_committees (list[str] | Unset):
    """

    code: str | Unset = UNSET
    name: str | Unset = UNSET
    name_genitive: str | Unset = UNSET
    type_: ComitteeType | Unset = UNSET
    phone: str | Unset = UNSET
    appointment_date: datetime.date | Unset = UNSET
    composition_date: datetime.date | Unset = UNSET
    scope: str | Unset = UNSET
    members: list[Member] | Unset = UNSET
    sub_committees: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        name = self.name

        name_genitive = self.name_genitive

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        phone = self.phone

        appointment_date: str | Unset = UNSET
        if not isinstance(self.appointment_date, Unset):
            appointment_date = self.appointment_date.isoformat()

        composition_date: str | Unset = UNSET
        if not isinstance(self.composition_date, Unset):
            composition_date = self.composition_date.isoformat()

        scope = self.scope

        members: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.members, Unset):
            members = []
            for members_item_data in self.members:
                members_item = members_item_data.to_dict()
                members.append(members_item)

        sub_committees: list[str] | Unset = UNSET
        if not isinstance(self.sub_committees, Unset):
            sub_committees = self.sub_committees

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if name is not UNSET:
            field_dict["name"] = name
        if name_genitive is not UNSET:
            field_dict["nameGenitive"] = name_genitive
        if type_ is not UNSET:
            field_dict["type"] = type_
        if phone is not UNSET:
            field_dict["phone"] = phone
        if appointment_date is not UNSET:
            field_dict["appointmentDate"] = appointment_date
        if composition_date is not UNSET:
            field_dict["compositionDate"] = composition_date
        if scope is not UNSET:
            field_dict["scope"] = scope
        if members is not UNSET:
            field_dict["members"] = members
        if sub_committees is not UNSET:
            field_dict["subCommittees"] = sub_committees

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.member import Member

        d = dict(src_dict)
        code = d.pop("code", UNSET)

        name = d.pop("name", UNSET)

        name_genitive = d.pop("nameGenitive", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: ComitteeType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ComitteeType(_type_)

        phone = d.pop("phone", UNSET)

        _appointment_date = d.pop("appointmentDate", UNSET)
        appointment_date: datetime.date | Unset
        if isinstance(_appointment_date, Unset):
            appointment_date = UNSET
        else:
            appointment_date = isoparse(_appointment_date).date()

        _composition_date = d.pop("compositionDate", UNSET)
        composition_date: datetime.date | Unset
        if isinstance(_composition_date, Unset):
            composition_date = UNSET
        else:
            composition_date = isoparse(_composition_date).date()

        scope = d.pop("scope", UNSET)

        _members = d.pop("members", UNSET)
        members: list[Member] | Unset = UNSET
        if _members is not UNSET:
            members = []
            for members_item_data in _members:
                members_item = Member.from_dict(members_item_data)

                members.append(members_item)

        sub_committees = cast(list[str], d.pop("subCommittees", UNSET))

        committee = cls(
            code=code,
            name=name,
            name_genitive=name_genitive,
            type_=type_,
            phone=phone,
            appointment_date=appointment_date,
            composition_date=composition_date,
            scope=scope,
            members=members,
            sub_committees=sub_committees,
        )

        committee.additional_properties = d
        return committee

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
