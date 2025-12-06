from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.print_info import PrintInfo


T = TypeVar("T", bound="Term")


@_attrs_define
class Term:
    """information about a term of the Sejm

    Attributes:
        num (int | Unset): Number of term of the Sejm Example: 9.
        from_ (datetime.date | Unset): Date start of term Example: 2019-11-12.
        to (datetime.date | Unset): Date end of term Example: 2019-11-12.
        current (bool | Unset): Current of term Example: True.
        prints (PrintInfo | Unset): info about prints
    """

    num: int | Unset = UNSET
    from_: datetime.date | Unset = UNSET
    to: datetime.date | Unset = UNSET
    current: bool | Unset = UNSET
    prints: PrintInfo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        num = self.num

        from_: str | Unset = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_.isoformat()

        to: str | Unset = UNSET
        if not isinstance(self.to, Unset):
            to = self.to.isoformat()

        current = self.current

        prints: dict[str, Any] | Unset = UNSET
        if not isinstance(self.prints, Unset):
            prints = self.prints.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if num is not UNSET:
            field_dict["num"] = num
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to
        if current is not UNSET:
            field_dict["current"] = current
        if prints is not UNSET:
            field_dict["prints"] = prints

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.print_info import PrintInfo

        d = dict(src_dict)
        num = d.pop("num", UNSET)

        _from_ = d.pop("from", UNSET)
        from_: datetime.date | Unset
        if isinstance(_from_, Unset):
            from_ = UNSET
        else:
            from_ = isoparse(_from_).date()

        _to = d.pop("to", UNSET)
        to: datetime.date | Unset
        if isinstance(_to, Unset):
            to = UNSET
        else:
            to = isoparse(_to).date()

        current = d.pop("current", UNSET)

        _prints = d.pop("prints", UNSET)
        prints: PrintInfo | Unset
        if isinstance(_prints, Unset):
            prints = UNSET
        else:
            prints = PrintInfo.from_dict(_prints)

        term = cls(
            num=num,
            from_=from_,
            to=to,
            current=current,
            prints=prints,
        )

        term.additional_properties = d
        return term

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
