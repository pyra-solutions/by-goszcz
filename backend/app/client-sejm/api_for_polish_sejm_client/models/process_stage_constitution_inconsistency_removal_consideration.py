from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.process_stage import ProcessStage


T = TypeVar("T", bound="ProcessStageConstitutionInconsistencyRemovalConsideration")


@_attrs_define
class ProcessStageConstitutionInconsistencyRemovalConsideration:
    """Consideration in the Sejm of the report of the committee on the removal of inconsistence with the Constitution

    Attributes:
        stage_name (str | Unset): a name of a stage Example: I czytanie na posiedzeniu Sejmu.
        date (datetime.date | Unset): a stage date Example: 2019-11-28.
        children (list[ProcessStage] | Unset): child stages
        sitting_num (int | Unset): Sejm sitting number Example: 10.
        decision (str | Unset): the Sejm decision Example: podjęto uchwałę.
        comment (str | Unset): a comment Example: Na 78. pos. Sejm podjął uchwałę w sprawie usunięcia niezgodności w
            ustawie.
        links (list[Any] | Unset): Link to resolution
        stage_type (str | Unset):
    """

    stage_name: str | Unset = UNSET
    date: datetime.date | Unset = UNSET
    children: list[ProcessStage] | Unset = UNSET
    sitting_num: int | Unset = UNSET
    decision: str | Unset = UNSET
    comment: str | Unset = UNSET
    links: list[Any] | Unset = UNSET
    stage_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stage_name = self.stage_name

        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        children: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.children, Unset):
            children = []
            for children_item_data in self.children:
                children_item = children_item_data.to_dict()
                children.append(children_item)

        sitting_num = self.sitting_num

        decision = self.decision

        comment = self.comment

        links: list[Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links

        stage_type = self.stage_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if stage_name is not UNSET:
            field_dict["stageName"] = stage_name
        if date is not UNSET:
            field_dict["date"] = date
        if children is not UNSET:
            field_dict["children"] = children
        if sitting_num is not UNSET:
            field_dict["sittingNum"] = sitting_num
        if decision is not UNSET:
            field_dict["decision"] = decision
        if comment is not UNSET:
            field_dict["comment"] = comment
        if links is not UNSET:
            field_dict["links"] = links
        if stage_type is not UNSET:
            field_dict["stageType"] = stage_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.process_stage import ProcessStage

        d = dict(src_dict)
        stage_name = d.pop("stageName", UNSET)

        _date = d.pop("date", UNSET)
        date: datetime.date | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()

        _children = d.pop("children", UNSET)
        children: list[ProcessStage] | Unset = UNSET
        if _children is not UNSET:
            children = []
            for children_item_data in _children:
                children_item = ProcessStage.from_dict(children_item_data)

                children.append(children_item)

        sitting_num = d.pop("sittingNum", UNSET)

        decision = d.pop("decision", UNSET)

        comment = d.pop("comment", UNSET)

        links = cast(list[Any], d.pop("links", UNSET))

        stage_type = d.pop("stageType", UNSET)

        process_stage_constitution_inconsistency_removal_consideration = cls(
            stage_name=stage_name,
            date=date,
            children=children,
            sitting_num=sitting_num,
            decision=decision,
            comment=comment,
            links=links,
            stage_type=stage_type,
        )

        process_stage_constitution_inconsistency_removal_consideration.additional_properties = d
        return process_stage_constitution_inconsistency_removal_consideration

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
