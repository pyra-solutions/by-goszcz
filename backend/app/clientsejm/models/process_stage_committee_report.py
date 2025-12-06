from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.process_document import ProcessDocument
    from ..models.process_stage import ProcessStage


T = TypeVar("T", bound="ProcessStageCommitteeReport")


@_attrs_define
class ProcessStageCommitteeReport:
    """committee report

    Attributes:
        stage_name (str | Unset): a name of a stage Example: I czytanie na posiedzeniu Sejmu.
        date (datetime.date | Unset): a stage date Example: 2019-11-28.
        children (list[ProcessStage] | Unset): child stages
        sub_committee (bool | Unset): is this subcommittee report
        report_file (str | Unset): an URL to a report
        print_number (str | Unset): a print number
        rapporteur_name (str | Unset): a name of the MP
        rapporteur_id (str | Unset): an ID of the MP
        minority_motions (int | Unset): number of minority motions
        proposal (str | Unset): commission proposal
        comment (str | Unset): commission proposal comment
        other_documents (list[ProcessDocument] | Unset): other documents, e.g. errata
        stage_type (str | Unset):
    """

    stage_name: str | Unset = UNSET
    date: datetime.date | Unset = UNSET
    children: list[ProcessStage] | Unset = UNSET
    sub_committee: bool | Unset = UNSET
    report_file: str | Unset = UNSET
    print_number: str | Unset = UNSET
    rapporteur_name: str | Unset = UNSET
    rapporteur_id: str | Unset = UNSET
    minority_motions: int | Unset = UNSET
    proposal: str | Unset = UNSET
    comment: str | Unset = UNSET
    other_documents: list[ProcessDocument] | Unset = UNSET
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

        sub_committee = self.sub_committee

        report_file = self.report_file

        print_number = self.print_number

        rapporteur_name = self.rapporteur_name

        rapporteur_id = self.rapporteur_id

        minority_motions = self.minority_motions

        proposal = self.proposal

        comment = self.comment

        other_documents: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.other_documents, Unset):
            other_documents = []
            for other_documents_item_data in self.other_documents:
                other_documents_item = other_documents_item_data.to_dict()
                other_documents.append(other_documents_item)

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
        if sub_committee is not UNSET:
            field_dict["subCommittee"] = sub_committee
        if report_file is not UNSET:
            field_dict["reportFile"] = report_file
        if print_number is not UNSET:
            field_dict["printNumber"] = print_number
        if rapporteur_name is not UNSET:
            field_dict["rapporteurName"] = rapporteur_name
        if rapporteur_id is not UNSET:
            field_dict["rapporteurID"] = rapporteur_id
        if minority_motions is not UNSET:
            field_dict["minorityMotions"] = minority_motions
        if proposal is not UNSET:
            field_dict["proposal"] = proposal
        if comment is not UNSET:
            field_dict["comment"] = comment
        if other_documents is not UNSET:
            field_dict["otherDocuments"] = other_documents
        if stage_type is not UNSET:
            field_dict["stageType"] = stage_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.process_document import ProcessDocument
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

        sub_committee = d.pop("subCommittee", UNSET)

        report_file = d.pop("reportFile", UNSET)

        print_number = d.pop("printNumber", UNSET)

        rapporteur_name = d.pop("rapporteurName", UNSET)

        rapporteur_id = d.pop("rapporteurID", UNSET)

        minority_motions = d.pop("minorityMotions", UNSET)

        proposal = d.pop("proposal", UNSET)

        comment = d.pop("comment", UNSET)

        _other_documents = d.pop("otherDocuments", UNSET)
        other_documents: list[ProcessDocument] | Unset = UNSET
        if _other_documents is not UNSET:
            other_documents = []
            for other_documents_item_data in _other_documents:
                other_documents_item = ProcessDocument.from_dict(other_documents_item_data)

                other_documents.append(other_documents_item)

        stage_type = d.pop("stageType", UNSET)

        process_stage_committee_report = cls(
            stage_name=stage_name,
            date=date,
            children=children,
            sub_committee=sub_committee,
            report_file=report_file,
            print_number=print_number,
            rapporteur_name=rapporteur_name,
            rapporteur_id=rapporteur_id,
            minority_motions=minority_motions,
            proposal=proposal,
            comment=comment,
            other_documents=other_documents,
            stage_type=stage_type,
        )

        process_stage_committee_report.additional_properties = d
        return process_stage_committee_report

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
