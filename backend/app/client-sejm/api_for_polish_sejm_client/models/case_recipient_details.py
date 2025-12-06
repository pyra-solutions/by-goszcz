from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CaseRecipientDetails")


@_attrs_define
class CaseRecipientDetails:
    """Details of a correspondence with a recipient

    Attributes:
        name (str | Unset): name of a recipient Example: prezes Rady Ministrów.
        sent (datetime.date | Unset): date when a case was sent Example: 2024-01-30.
        answer_delayed_days (int | Unset): number of days an answer is delayed for a given case. When an answer was
            given then the delay is set to 0. Example: 300.
    """

    name: str | Unset = UNSET
    sent: datetime.date | Unset = UNSET
    answer_delayed_days: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        sent: str | Unset = UNSET
        if not isinstance(self.sent, Unset):
            sent = self.sent.isoformat()

        answer_delayed_days = self.answer_delayed_days

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if sent is not UNSET:
            field_dict["sent"] = sent
        if answer_delayed_days is not UNSET:
            field_dict["answerDelayedDays"] = answer_delayed_days

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _sent = d.pop("sent", UNSET)
        sent: datetime.date | Unset
        if isinstance(_sent, Unset):
            sent = UNSET
        else:
            sent = isoparse(_sent).date()

        answer_delayed_days = d.pop("answerDelayedDays", UNSET)

        case_recipient_details = cls(
            name=name,
            sent=sent,
            answer_delayed_days=answer_delayed_days,
        )

        case_recipient_details.additional_properties = d
        return case_recipient_details

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
