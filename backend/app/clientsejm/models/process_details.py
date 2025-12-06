from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.process_type import ProcessType
from ..models.ue_status import UEStatus
from ..models.urgency_status import UrgencyStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.process_document import ProcessDocument
    from ..models.process_stage import ProcessStage


T = TypeVar("T", bound="ProcessDetails")


@_attrs_define
class ProcessDetails:
    """A details of legislative process

    Attributes:
        term (int | Unset): a Sejm term Example: 9.
        number (str | Unset): a number of a print in the specified Sejm term Example: 19.
        title (str | Unset): a title of a process Example: Rządowy projekt ustawy o zmianie ustawy o transporcie
            kolejowym.
        description (str | Unset): a description of a process Example: projekt ustawy dotyczy utworzenia nowego
            uniwersytetu medycznego.
        u_e (UEStatus | Unset):
        document_date (datetime.date | Unset): a date of a print Example: 2019-11-19.
        change_date (datetime.datetime | Unset): a date of last change to the process Example: 2019-11-21 10:01:37.
        web_generated_date (datetime.datetime | Unset): A date when a web page with a process was updated Example:
            2020-01-02 15:00:52.
        process_start_date (datetime.date | Unset): a date of the start of the process Example: 2019-11-19.
        document_type (str | Unset): a type of a document Example: projekt ustawy.
        document_type_enum (ProcessType | Unset):
        comments (str | Unset): comments Example: Obywatelski projekt ustawy został wniesiony w VIII kadencji Sejmu
            (druk nr 226). Na podstawie art. 4. ust. 3 ustawy o wykonywaniu inicjatywy ustawodawczej przez obywateli -
            projekt ustawy, w stosunku do którego postępowanie ustawodawcze nie zostało zakończone w trakcie kadencji Sejmu,
            w której został wniesiony, jest rozpatrywany przez Sejm następnej kadencji..
        prints_considered_jointly (list[str] | Unset): prints considered jointly
        title_final (str | Unset): A final title of the act Example: o zmianie ustawy o świadczeniach opieki zdrowotnej
            finansowanych ze środków publicznych.
        closure_date (datetime.date | Unset): A date of case closure Example: 2023-11-29.
        address (str | Unset): an address of publication in the ISAP service. An address is in format
            {publisher}{year}{volume}{position} Example: WDU20250000179.
        display_address (str | Unset): an address to display Example: Dz.U. 2025 poz. 179.
        e_li (str | Unset): an European Legislation Identifier Example: DU/2025/179.
        passed (bool | Unset): is this act was passed Example: True.
        links (list[Any] | Unset): Links
        shorten_procedure (bool | Unset): Article 51 of the Sejm Regulations - in particularly justified cases, the Sejm
            may shorten the procedure for drafting bills
        urgency_status (UrgencyStatus | Unset):
        urgency_withdraw_date (datetime.date | Unset): date when urgency clause was withdrawn Example: 2022-03-10.
        other_documents (list[ProcessDocument] | Unset): other prints, corrections
        rcl_num (str | Unset): number from government part of the process (from RCL website) Example: RM-0610-84-21.
        rcl_link (str | Unset): link to government part of the process (RCL website)
        legislative_committee (bool | Unset): indicates that for work on this project a members of Legislative Committee
            has been assigned
        principle_of_subsidiarity (bool | Unset): indicates that the project is inconsistent with the principle of
            subsidiarity
        stages (list[ProcessStage] | Unset): stages of the process
    """

    term: int | Unset = UNSET
    number: str | Unset = UNSET
    title: str | Unset = UNSET
    description: str | Unset = UNSET
    u_e: UEStatus | Unset = UNSET
    document_date: datetime.date | Unset = UNSET
    change_date: datetime.datetime | Unset = UNSET
    web_generated_date: datetime.datetime | Unset = UNSET
    process_start_date: datetime.date | Unset = UNSET
    document_type: str | Unset = UNSET
    document_type_enum: ProcessType | Unset = UNSET
    comments: str | Unset = UNSET
    prints_considered_jointly: list[str] | Unset = UNSET
    title_final: str | Unset = UNSET
    closure_date: datetime.date | Unset = UNSET
    address: str | Unset = UNSET
    display_address: str | Unset = UNSET
    e_li: str | Unset = UNSET
    passed: bool | Unset = UNSET
    links: list[Any] | Unset = UNSET
    shorten_procedure: bool | Unset = UNSET
    urgency_status: UrgencyStatus | Unset = UNSET
    urgency_withdraw_date: datetime.date | Unset = UNSET
    other_documents: list[ProcessDocument] | Unset = UNSET
    rcl_num: str | Unset = UNSET
    rcl_link: str | Unset = UNSET
    legislative_committee: bool | Unset = UNSET
    principle_of_subsidiarity: bool | Unset = UNSET
    stages: list[ProcessStage] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        term = self.term

        number = self.number

        title = self.title

        description = self.description

        u_e: str | Unset = UNSET
        if not isinstance(self.u_e, Unset):
            u_e = self.u_e.value

        document_date: str | Unset = UNSET
        if not isinstance(self.document_date, Unset):
            document_date = self.document_date.isoformat()

        change_date: str | Unset = UNSET
        if not isinstance(self.change_date, Unset):
            change_date = self.change_date.isoformat()

        web_generated_date: str | Unset = UNSET
        if not isinstance(self.web_generated_date, Unset):
            web_generated_date = self.web_generated_date.isoformat()

        process_start_date: str | Unset = UNSET
        if not isinstance(self.process_start_date, Unset):
            process_start_date = self.process_start_date.isoformat()

        document_type = self.document_type

        document_type_enum: str | Unset = UNSET
        if not isinstance(self.document_type_enum, Unset):
            document_type_enum = self.document_type_enum.value

        comments = self.comments

        prints_considered_jointly: list[str] | Unset = UNSET
        if not isinstance(self.prints_considered_jointly, Unset):
            prints_considered_jointly = self.prints_considered_jointly

        title_final = self.title_final

        closure_date: str | Unset = UNSET
        if not isinstance(self.closure_date, Unset):
            closure_date = self.closure_date.isoformat()

        address = self.address

        display_address = self.display_address

        e_li = self.e_li

        passed = self.passed

        links: list[Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links

        shorten_procedure = self.shorten_procedure

        urgency_status: str | Unset = UNSET
        if not isinstance(self.urgency_status, Unset):
            urgency_status = self.urgency_status.value

        urgency_withdraw_date: str | Unset = UNSET
        if not isinstance(self.urgency_withdraw_date, Unset):
            urgency_withdraw_date = self.urgency_withdraw_date.isoformat()

        other_documents: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.other_documents, Unset):
            other_documents = []
            for other_documents_item_data in self.other_documents:
                other_documents_item = other_documents_item_data.to_dict()
                other_documents.append(other_documents_item)

        rcl_num = self.rcl_num

        rcl_link = self.rcl_link

        legislative_committee = self.legislative_committee

        principle_of_subsidiarity = self.principle_of_subsidiarity

        stages: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.stages, Unset):
            stages = []
            for stages_item_data in self.stages:
                stages_item = stages_item_data.to_dict()
                stages.append(stages_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if term is not UNSET:
            field_dict["term"] = term
        if number is not UNSET:
            field_dict["number"] = number
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if u_e is not UNSET:
            field_dict["uE"] = u_e
        if document_date is not UNSET:
            field_dict["documentDate"] = document_date
        if change_date is not UNSET:
            field_dict["changeDate"] = change_date
        if web_generated_date is not UNSET:
            field_dict["webGeneratedDate"] = web_generated_date
        if process_start_date is not UNSET:
            field_dict["processStartDate"] = process_start_date
        if document_type is not UNSET:
            field_dict["documentType"] = document_type
        if document_type_enum is not UNSET:
            field_dict["documentTypeEnum"] = document_type_enum
        if comments is not UNSET:
            field_dict["comments"] = comments
        if prints_considered_jointly is not UNSET:
            field_dict["printsConsideredJointly"] = prints_considered_jointly
        if title_final is not UNSET:
            field_dict["titleFinal"] = title_final
        if closure_date is not UNSET:
            field_dict["closureDate"] = closure_date
        if address is not UNSET:
            field_dict["address"] = address
        if display_address is not UNSET:
            field_dict["displayAddress"] = display_address
        if e_li is not UNSET:
            field_dict["eLI"] = e_li
        if passed is not UNSET:
            field_dict["passed"] = passed
        if links is not UNSET:
            field_dict["links"] = links
        if shorten_procedure is not UNSET:
            field_dict["shortenProcedure"] = shorten_procedure
        if urgency_status is not UNSET:
            field_dict["urgencyStatus"] = urgency_status
        if urgency_withdraw_date is not UNSET:
            field_dict["urgencyWithdrawDate"] = urgency_withdraw_date
        if other_documents is not UNSET:
            field_dict["otherDocuments"] = other_documents
        if rcl_num is not UNSET:
            field_dict["rclNum"] = rcl_num
        if rcl_link is not UNSET:
            field_dict["rclLink"] = rcl_link
        if legislative_committee is not UNSET:
            field_dict["legislativeCommittee"] = legislative_committee
        if principle_of_subsidiarity is not UNSET:
            field_dict["principleOfSubsidiarity"] = principle_of_subsidiarity
        if stages is not UNSET:
            field_dict["stages"] = stages

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.process_document import ProcessDocument
        from ..models.process_stage import ProcessStage

        d = dict(src_dict)
        term = d.pop("term", UNSET)

        number = d.pop("number", UNSET)

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        _u_e = d.pop("uE", UNSET)
        u_e: UEStatus | Unset
        if isinstance(_u_e, Unset):
            u_e = UNSET
        else:
            u_e = UEStatus(_u_e)

        _document_date = d.pop("documentDate", UNSET)
        document_date: datetime.date | Unset
        if isinstance(_document_date, Unset):
            document_date = UNSET
        else:
            document_date = isoparse(_document_date).date()

        _change_date = d.pop("changeDate", UNSET)
        change_date: datetime.datetime | Unset
        if isinstance(_change_date, Unset):
            change_date = UNSET
        else:
            change_date = isoparse(_change_date)

        _web_generated_date = d.pop("webGeneratedDate", UNSET)
        web_generated_date: datetime.datetime | Unset
        if isinstance(_web_generated_date, Unset):
            web_generated_date = UNSET
        else:
            web_generated_date = isoparse(_web_generated_date)

        _process_start_date = d.pop("processStartDate", UNSET)
        process_start_date: datetime.date | Unset
        if isinstance(_process_start_date, Unset):
            process_start_date = UNSET
        else:
            process_start_date = isoparse(_process_start_date).date()

        document_type = d.pop("documentType", UNSET)

        _document_type_enum = d.pop("documentTypeEnum", UNSET)
        document_type_enum: ProcessType | Unset
        if isinstance(_document_type_enum, Unset):
            document_type_enum = UNSET
        else:
            document_type_enum = ProcessType(_document_type_enum)

        comments = d.pop("comments", UNSET)

        prints_considered_jointly = cast(list[str], d.pop("printsConsideredJointly", UNSET))

        title_final = d.pop("titleFinal", UNSET)

        _closure_date = d.pop("closureDate", UNSET)
        closure_date: datetime.date | Unset
        if isinstance(_closure_date, Unset):
            closure_date = UNSET
        else:
            closure_date = isoparse(_closure_date).date()

        address = d.pop("address", UNSET)

        display_address = d.pop("displayAddress", UNSET)

        e_li = d.pop("eLI", UNSET)

        passed = d.pop("passed", UNSET)

        links = cast(list[Any], d.pop("links", UNSET))

        shorten_procedure = d.pop("shortenProcedure", UNSET)

        _urgency_status = d.pop("urgencyStatus", UNSET)
        urgency_status: UrgencyStatus | Unset
        if isinstance(_urgency_status, Unset):
            urgency_status = UNSET
        else:
            urgency_status = UrgencyStatus(_urgency_status)

        _urgency_withdraw_date = d.pop("urgencyWithdrawDate", UNSET)
        urgency_withdraw_date: datetime.date | Unset
        if isinstance(_urgency_withdraw_date, Unset):
            urgency_withdraw_date = UNSET
        else:
            urgency_withdraw_date = isoparse(_urgency_withdraw_date).date()

        _other_documents = d.pop("otherDocuments", UNSET)
        other_documents: list[ProcessDocument] | Unset = UNSET
        if _other_documents is not UNSET:
            other_documents = []
            for other_documents_item_data in _other_documents:
                other_documents_item = ProcessDocument.from_dict(other_documents_item_data)

                other_documents.append(other_documents_item)

        rcl_num = d.pop("rclNum", UNSET)

        rcl_link = d.pop("rclLink", UNSET)

        legislative_committee = d.pop("legislativeCommittee", UNSET)

        principle_of_subsidiarity = d.pop("principleOfSubsidiarity", UNSET)

        _stages = d.pop("stages", UNSET)
        stages: list[ProcessStage] | Unset = UNSET
        if _stages is not UNSET:
            stages = []
            for stages_item_data in _stages:
                stages_item = ProcessStage.from_dict(stages_item_data)

                stages.append(stages_item)

        process_details = cls(
            term=term,
            number=number,
            title=title,
            description=description,
            u_e=u_e,
            document_date=document_date,
            change_date=change_date,
            web_generated_date=web_generated_date,
            process_start_date=process_start_date,
            document_type=document_type,
            document_type_enum=document_type_enum,
            comments=comments,
            prints_considered_jointly=prints_considered_jointly,
            title_final=title_final,
            closure_date=closure_date,
            address=address,
            display_address=display_address,
            e_li=e_li,
            passed=passed,
            links=links,
            shorten_procedure=shorten_procedure,
            urgency_status=urgency_status,
            urgency_withdraw_date=urgency_withdraw_date,
            other_documents=other_documents,
            rcl_num=rcl_num,
            rcl_link=rcl_link,
            legislative_committee=legislative_committee,
            principle_of_subsidiarity=principle_of_subsidiarity,
            stages=stages,
        )

        process_details.additional_properties = d
        return process_details

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
