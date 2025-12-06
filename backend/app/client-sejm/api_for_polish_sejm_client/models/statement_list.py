from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.statement import Statement


T = TypeVar("T", bound="StatementList")


@_attrs_define
class StatementList:
    """
    Attributes:
        proceeding_num (int | Unset):
        date (datetime.date | Unset):  Example: 2022-03-10.
        statements (list[Statement] | Unset):
    """

    proceeding_num: int | Unset = UNSET
    date: datetime.date | Unset = UNSET
    statements: list[Statement] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        proceeding_num = self.proceeding_num

        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        statements: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.statements, Unset):
            statements = []
            for statements_item_data in self.statements:
                statements_item = statements_item_data.to_dict()
                statements.append(statements_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if proceeding_num is not UNSET:
            field_dict["proceedingNum"] = proceeding_num
        if date is not UNSET:
            field_dict["date"] = date
        if statements is not UNSET:
            field_dict["statements"] = statements

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.statement import Statement

        d = dict(src_dict)
        proceeding_num = d.pop("proceedingNum", UNSET)

        _date = d.pop("date", UNSET)
        date: datetime.date | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()

        _statements = d.pop("statements", UNSET)
        statements: list[Statement] | Unset = UNSET
        if _statements is not UNSET:
            statements = []
            for statements_item_data in _statements:
                statements_item = Statement.from_dict(statements_item_data)

                statements.append(statements_item)

        statement_list = cls(
            proceeding_num=proceeding_num,
            date=date,
            statements=statements,
        )

        statement_list.additional_properties = d
        return statement_list

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
