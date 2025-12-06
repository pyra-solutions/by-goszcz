from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Member")


@_attrs_define
class Member:
    """A member of a committee or a parliamentary team.

    Attributes:
        id (int | Unset): A number of the identity card of the MP.
        last_first_name (str | Unset): The last and first name of the MP.
        function (str | Unset): A function in the committee.
        mandate_expired (datetime.date | Unset): A date of expiry of the parliamentary mandate. Example: 2022-03-10.
        club (str | Unset): A club to where MP is belonging
    """

    id: int | Unset = UNSET
    last_first_name: str | Unset = UNSET
    function: str | Unset = UNSET
    mandate_expired: datetime.date | Unset = UNSET
    club: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        last_first_name = self.last_first_name

        function = self.function

        mandate_expired: str | Unset = UNSET
        if not isinstance(self.mandate_expired, Unset):
            mandate_expired = self.mandate_expired.isoformat()

        club = self.club

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if last_first_name is not UNSET:
            field_dict["lastFirstName"] = last_first_name
        if function is not UNSET:
            field_dict["function"] = function
        if mandate_expired is not UNSET:
            field_dict["mandateExpired"] = mandate_expired
        if club is not UNSET:
            field_dict["club"] = club

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        last_first_name = d.pop("lastFirstName", UNSET)

        function = d.pop("function", UNSET)

        _mandate_expired = d.pop("mandateExpired", UNSET)
        mandate_expired: datetime.date | Unset
        if isinstance(_mandate_expired, Unset):
            mandate_expired = UNSET
        else:
            mandate_expired = isoparse(_mandate_expired).date()

        club = d.pop("club", UNSET)

        member = cls(
            id=id,
            last_first_name=last_first_name,
            function=function,
            mandate_expired=mandate_expired,
            club=club,
        )

        member.additional_properties = d
        return member

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
