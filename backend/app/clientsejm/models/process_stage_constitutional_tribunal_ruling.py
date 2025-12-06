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


T = TypeVar("T", bound="ProcessStageConstitutionalTribunalRuling")


@_attrs_define
class ProcessStageConstitutionalTribunalRuling:
    """The Constitutional Tribunal ruling

    Attributes:
        stage_name (str | Unset): a name of a stage Example: I czytanie na posiedzeniu Sejmu.
        date (datetime.date | Unset): a stage date Example: 2019-11-28.
        children (list[ProcessStage] | Unset): child stages
        publisher (str | Unset): a code of a publisher Example: WDU.
        publication_year (str | Unset): a year of publication Example: 2020.
        publication_number (str | Unset): a volume of a publication. Specifies a volume in year. After year 2012 there
            are no volumes and this field should have value '0'. Example: 0.
        publication_position (str | Unset): a position in a year Example: 647.
        verdict (str | Unset): a Constitutional Tribunal verdict Example: Ustawa jest w całości niezgodna z art. 7 w
            związku z art. 112 oraz z art. 119 ust. 1 Konstytucji RP.
        links (list[Any] | Unset): Links to HTML pages
        stage_type (str | Unset):
    """

    stage_name: str | Unset = UNSET
    date: datetime.date | Unset = UNSET
    children: list[ProcessStage] | Unset = UNSET
    publisher: str | Unset = UNSET
    publication_year: str | Unset = UNSET
    publication_number: str | Unset = UNSET
    publication_position: str | Unset = UNSET
    verdict: str | Unset = UNSET
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

        publisher = self.publisher

        publication_year = self.publication_year

        publication_number = self.publication_number

        publication_position = self.publication_position

        verdict = self.verdict

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
        if publisher is not UNSET:
            field_dict["publisher"] = publisher
        if publication_year is not UNSET:
            field_dict["publicationYear"] = publication_year
        if publication_number is not UNSET:
            field_dict["publicationNumber"] = publication_number
        if publication_position is not UNSET:
            field_dict["publicationPosition"] = publication_position
        if verdict is not UNSET:
            field_dict["verdict"] = verdict
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

        publisher = d.pop("publisher", UNSET)

        publication_year = d.pop("publicationYear", UNSET)

        publication_number = d.pop("publicationNumber", UNSET)

        publication_position = d.pop("publicationPosition", UNSET)

        verdict = d.pop("verdict", UNSET)

        links = cast(list[Any], d.pop("links", UNSET))

        stage_type = d.pop("stageType", UNSET)

        process_stage_constitutional_tribunal_ruling = cls(
            stage_name=stage_name,
            date=date,
            children=children,
            publisher=publisher,
            publication_year=publication_year,
            publication_number=publication_number,
            publication_position=publication_position,
            verdict=verdict,
            links=links,
            stage_type=stage_type,
        )

        process_stage_constitutional_tribunal_ruling.additional_properties = d
        return process_stage_constitutional_tribunal_ruling

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
