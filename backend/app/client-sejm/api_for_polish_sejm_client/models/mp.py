from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="MP")


@_attrs_define
class MP:
    """A MP.

    Attributes:
        id (int | Unset): A number of the identity card of the MP. Example: 103.
        first_last_name (str | Unset): The first and last name of the MP. Example: Marta Golbik.
        last_first_name (str | Unset): The last and first name of the MP. Example: Golbik Marta.
        first_name (str | Unset): The first name of the MP. Example: Marta.
        second_name (str | Unset): The second name of the MP. Example: Joanna.
        last_name (str | Unset): The last name of the MP. Example: Golbik.
        genitive_name (str | Unset): The first and last name in genitive case. Example: Marty Golbik.
        accusative_name (str | Unset): The first and last name in accusative case. Example: Martę Golbik.
        email (str | Unset): The email of the MP. Example: Marta.Golbik@sejm.pl.
        active (bool | Unset): Is the MP active? Example: True.
        inactive_cause (str | Unset): The cause of inactivity Example: Zrzeczenie.
        waiver_desc (str | Unset): ?
        district_num (int | Unset): A district id where MP was elected Example: 29.
        district_name (str | Unset): A district name where MP was elected Example: Katowice.
        voivodeship (str | Unset): A voivodeship where MP was elected Example: śląskie.
        club (str | Unset): A club to where MP is belonging Example: KO.
        birth_date (datetime.date | Unset): a date of birth Example: 1985-04-14.
        birth_location (str | Unset): a place of birth Example: Gliwice.
        profession (str | Unset): a profession Example: przedsiębiorca prywatny.
        education_level (str | Unset): an education level Example: wyższe.
        number_of_votes (int | Unset): a number of votes Example: 19430.
    """

    id: int | Unset = UNSET
    first_last_name: str | Unset = UNSET
    last_first_name: str | Unset = UNSET
    first_name: str | Unset = UNSET
    second_name: str | Unset = UNSET
    last_name: str | Unset = UNSET
    genitive_name: str | Unset = UNSET
    accusative_name: str | Unset = UNSET
    email: str | Unset = UNSET
    active: bool | Unset = UNSET
    inactive_cause: str | Unset = UNSET
    waiver_desc: str | Unset = UNSET
    district_num: int | Unset = UNSET
    district_name: str | Unset = UNSET
    voivodeship: str | Unset = UNSET
    club: str | Unset = UNSET
    birth_date: datetime.date | Unset = UNSET
    birth_location: str | Unset = UNSET
    profession: str | Unset = UNSET
    education_level: str | Unset = UNSET
    number_of_votes: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        first_last_name = self.first_last_name

        last_first_name = self.last_first_name

        first_name = self.first_name

        second_name = self.second_name

        last_name = self.last_name

        genitive_name = self.genitive_name

        accusative_name = self.accusative_name

        email = self.email

        active = self.active

        inactive_cause = self.inactive_cause

        waiver_desc = self.waiver_desc

        district_num = self.district_num

        district_name = self.district_name

        voivodeship = self.voivodeship

        club = self.club

        birth_date: str | Unset = UNSET
        if not isinstance(self.birth_date, Unset):
            birth_date = self.birth_date.isoformat()

        birth_location = self.birth_location

        profession = self.profession

        education_level = self.education_level

        number_of_votes = self.number_of_votes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if first_last_name is not UNSET:
            field_dict["firstLastName"] = first_last_name
        if last_first_name is not UNSET:
            field_dict["lastFirstName"] = last_first_name
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if second_name is not UNSET:
            field_dict["secondName"] = second_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if genitive_name is not UNSET:
            field_dict["genitiveName"] = genitive_name
        if accusative_name is not UNSET:
            field_dict["accusativeName"] = accusative_name
        if email is not UNSET:
            field_dict["email"] = email
        if active is not UNSET:
            field_dict["active"] = active
        if inactive_cause is not UNSET:
            field_dict["inactiveCause"] = inactive_cause
        if waiver_desc is not UNSET:
            field_dict["waiverDesc"] = waiver_desc
        if district_num is not UNSET:
            field_dict["districtNum"] = district_num
        if district_name is not UNSET:
            field_dict["districtName"] = district_name
        if voivodeship is not UNSET:
            field_dict["voivodeship"] = voivodeship
        if club is not UNSET:
            field_dict["club"] = club
        if birth_date is not UNSET:
            field_dict["birthDate"] = birth_date
        if birth_location is not UNSET:
            field_dict["birthLocation"] = birth_location
        if profession is not UNSET:
            field_dict["profession"] = profession
        if education_level is not UNSET:
            field_dict["educationLevel"] = education_level
        if number_of_votes is not UNSET:
            field_dict["numberOfVotes"] = number_of_votes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        first_last_name = d.pop("firstLastName", UNSET)

        last_first_name = d.pop("lastFirstName", UNSET)

        first_name = d.pop("firstName", UNSET)

        second_name = d.pop("secondName", UNSET)

        last_name = d.pop("lastName", UNSET)

        genitive_name = d.pop("genitiveName", UNSET)

        accusative_name = d.pop("accusativeName", UNSET)

        email = d.pop("email", UNSET)

        active = d.pop("active", UNSET)

        inactive_cause = d.pop("inactiveCause", UNSET)

        waiver_desc = d.pop("waiverDesc", UNSET)

        district_num = d.pop("districtNum", UNSET)

        district_name = d.pop("districtName", UNSET)

        voivodeship = d.pop("voivodeship", UNSET)

        club = d.pop("club", UNSET)

        _birth_date = d.pop("birthDate", UNSET)
        birth_date: datetime.date | Unset
        if isinstance(_birth_date, Unset):
            birth_date = UNSET
        else:
            birth_date = isoparse(_birth_date).date()

        birth_location = d.pop("birthLocation", UNSET)

        profession = d.pop("profession", UNSET)

        education_level = d.pop("educationLevel", UNSET)

        number_of_votes = d.pop("numberOfVotes", UNSET)

        mp = cls(
            id=id,
            first_last_name=first_last_name,
            last_first_name=last_first_name,
            first_name=first_name,
            second_name=second_name,
            last_name=last_name,
            genitive_name=genitive_name,
            accusative_name=accusative_name,
            email=email,
            active=active,
            inactive_cause=inactive_cause,
            waiver_desc=waiver_desc,
            district_num=district_num,
            district_name=district_name,
            voivodeship=voivodeship,
            club=club,
            birth_date=birth_date,
            birth_location=birth_location,
            profession=profession,
            education_level=education_level,
            number_of_votes=number_of_votes,
        )

        mp.additional_properties = d
        return mp

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
