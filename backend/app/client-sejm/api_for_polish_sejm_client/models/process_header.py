from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.process_type import ProcessType
from ..models.ue_status import UEStatus
from ..models.urgency_status import UrgencyStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProcessHeader")


@_attrs_define
class ProcessHeader:
    """A legislative process

    Attributes:
        u_e (UEStatus | Unset):
        e_li (str | Unset): an European Legislation Identifier Example: DU/2025/179.
        term (int | Unset): A Sejm term Example: 9.
        number (str | Unset): A number of the process Example: 40.
        title (str | Unset): A title of the process Example: Obywatelski projekt ustawy o ochronie własności w
            Rzeczypospolitej Polskiej przed roszczeniami dotyczącymi mienia bezdziedzicznego.
        title_final (str | Unset): A final title of the act Example: o zmianie ustawy o świadczeniach opieki zdrowotnej
            finansowanych ze środków publicznych.
        description (str | Unset): A description of the process Example: projekt dotyczy zawieszenia na okres 6 miesięcy
            2020 r. funkcjonowania ustawy. Przepisy ustawy będą stosowane do przychodów ze sprzedaży detalicznej
            osiągniętych od 1 lipca 2020 r.
        ue (UEStatus | Unset):
        document_date (datetime.date | Unset): A date of document Example: 2019-11-28.
        process_start_date (datetime.date | Unset): Process start date Example: 2019-11-28.
        change_date (datetime.datetime | Unset): A date when a process was last changed Example: 2020-01-02 15:00:52.
        document_type (str | Unset): A document type Example: projekt ustawy.
        document_type_enum (ProcessType | Unset):
        comments (str | Unset): Comments Example: Obywatelski projekt ustawy został wniesiony w VIII kadencji Sejmu
            (druk nr 226). Na podstawie art. 4. ust. 3 ustawy o wykonywaniu inicjatywy ustawodawczej przez obywateli -
            projekt ustawy, w stosunku do którego postępowanie ustawodawcze nie zostało zakończone w trakcie kadencji Sejmu,
            w której został wniesiony, jest rozpatrywany przez Sejm następnej kadencji..
        web_generated_date (datetime.datetime | Unset): A date when a web page with a process was updated Example:
            2020-01-02 15:00:52.
        closure_date (datetime.date | Unset): A date of case closure Example: 2023-11-29.
        address (str | Unset): an address of publication in the ISAP service. An address is in format
            {publisher}{year}{volume}{position} Example: WDU20250000179.
        display_address (str | Unset): an address to display Example: Dz.U. 2025 poz. 179.
        eli (str | Unset): an European Legislation Identifier Example: DU/2025/179.
        passed (bool | Unset): is this act was passed Example: True.
        links (list[Any] | Unset): Links
        shorten_procedure (bool | Unset): Article 51 of the Sejm Regulations - in particularly justified cases, the Sejm
            may shorten the procedure for drafting bills
        urgency_status (UrgencyStatus | Unset):
        urgency_withdraw_date (datetime.date | Unset): date when urgency clause was withdrawn Example: 2022-03-10.
        prints_considered_jointly (list[str] | Unset): prints considered jointly
    """

    u_e: UEStatus | Unset = UNSET
    e_li: str | Unset = UNSET
    term: int | Unset = UNSET
    number: str | Unset = UNSET
    title: str | Unset = UNSET
    title_final: str | Unset = UNSET
    description: str | Unset = UNSET
    ue: UEStatus | Unset = UNSET
    document_date: datetime.date | Unset = UNSET
    process_start_date: datetime.date | Unset = UNSET
    change_date: datetime.datetime | Unset = UNSET
    document_type: str | Unset = UNSET
    document_type_enum: ProcessType | Unset = UNSET
    comments: str | Unset = UNSET
    web_generated_date: datetime.datetime | Unset = UNSET
    closure_date: datetime.date | Unset = UNSET
    address: str | Unset = UNSET
    display_address: str | Unset = UNSET
    eli: str | Unset = UNSET
    passed: bool | Unset = UNSET
    links: list[Any] | Unset = UNSET
    shorten_procedure: bool | Unset = UNSET
    urgency_status: UrgencyStatus | Unset = UNSET
    urgency_withdraw_date: datetime.date | Unset = UNSET
    prints_considered_jointly: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        u_e: str | Unset = UNSET
        if not isinstance(self.u_e, Unset):
            u_e = self.u_e.value

        e_li = self.e_li

        term = self.term

        number = self.number

        title = self.title

        title_final = self.title_final

        description = self.description

        ue: str | Unset = UNSET
        if not isinstance(self.ue, Unset):
            ue = self.ue.value

        document_date: str | Unset = UNSET
        if not isinstance(self.document_date, Unset):
            document_date = self.document_date.isoformat()

        process_start_date: str | Unset = UNSET
        if not isinstance(self.process_start_date, Unset):
            process_start_date = self.process_start_date.isoformat()

        change_date: str | Unset = UNSET
        if not isinstance(self.change_date, Unset):
            change_date = self.change_date.isoformat()

        document_type = self.document_type

        document_type_enum: str | Unset = UNSET
        if not isinstance(self.document_type_enum, Unset):
            document_type_enum = self.document_type_enum.value

        comments = self.comments

        web_generated_date: str | Unset = UNSET
        if not isinstance(self.web_generated_date, Unset):
            web_generated_date = self.web_generated_date.isoformat()

        closure_date: str | Unset = UNSET
        if not isinstance(self.closure_date, Unset):
            closure_date = self.closure_date.isoformat()

        address = self.address

        display_address = self.display_address

        eli = self.eli

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

        prints_considered_jointly: list[str] | Unset = UNSET
        if not isinstance(self.prints_considered_jointly, Unset):
            prints_considered_jointly = self.prints_considered_jointly

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if u_e is not UNSET:
            field_dict["uE"] = u_e
        if e_li is not UNSET:
            field_dict["eLI"] = e_li
        if term is not UNSET:
            field_dict["term"] = term
        if number is not UNSET:
            field_dict["number"] = number
        if title is not UNSET:
            field_dict["title"] = title
        if title_final is not UNSET:
            field_dict["titleFinal"] = title_final
        if description is not UNSET:
            field_dict["description"] = description
        if ue is not UNSET:
            field_dict["ue"] = ue
        if document_date is not UNSET:
            field_dict["documentDate"] = document_date
        if process_start_date is not UNSET:
            field_dict["processStartDate"] = process_start_date
        if change_date is not UNSET:
            field_dict["changeDate"] = change_date
        if document_type is not UNSET:
            field_dict["documentType"] = document_type
        if document_type_enum is not UNSET:
            field_dict["documentTypeEnum"] = document_type_enum
        if comments is not UNSET:
            field_dict["comments"] = comments
        if web_generated_date is not UNSET:
            field_dict["webGeneratedDate"] = web_generated_date
        if closure_date is not UNSET:
            field_dict["closureDate"] = closure_date
        if address is not UNSET:
            field_dict["address"] = address
        if display_address is not UNSET:
            field_dict["displayAddress"] = display_address
        if eli is not UNSET:
            field_dict["ELI"] = eli
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
        if prints_considered_jointly is not UNSET:
            field_dict["printsConsideredJointly"] = prints_considered_jointly

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _u_e = d.pop("uE", UNSET)
        u_e: UEStatus | Unset
        if isinstance(_u_e, Unset):
            u_e = UNSET
        else:
            u_e = UEStatus(_u_e)

        e_li = d.pop("eLI", UNSET)

        term = d.pop("term", UNSET)

        number = d.pop("number", UNSET)

        title = d.pop("title", UNSET)

        title_final = d.pop("titleFinal", UNSET)

        description = d.pop("description", UNSET)

        _ue = d.pop("ue", UNSET)
        ue: UEStatus | Unset
        if isinstance(_ue, Unset):
            ue = UNSET
        else:
            ue = UEStatus(_ue)

        _document_date = d.pop("documentDate", UNSET)
        document_date: datetime.date | Unset
        if isinstance(_document_date, Unset):
            document_date = UNSET
        else:
            document_date = isoparse(_document_date).date()

        _process_start_date = d.pop("processStartDate", UNSET)
        process_start_date: datetime.date | Unset
        if isinstance(_process_start_date, Unset):
            process_start_date = UNSET
        else:
            process_start_date = isoparse(_process_start_date).date()

        _change_date = d.pop("changeDate", UNSET)
        change_date: datetime.datetime | Unset
        if isinstance(_change_date, Unset):
            change_date = UNSET
        else:
            change_date = isoparse(_change_date)

        document_type = d.pop("documentType", UNSET)

        _document_type_enum = d.pop("documentTypeEnum", UNSET)
        document_type_enum: ProcessType | Unset
        if isinstance(_document_type_enum, Unset):
            document_type_enum = UNSET
        else:
            document_type_enum = ProcessType(_document_type_enum)

        comments = d.pop("comments", UNSET)

        _web_generated_date = d.pop("webGeneratedDate", UNSET)
        web_generated_date: datetime.datetime | Unset
        if isinstance(_web_generated_date, Unset):
            web_generated_date = UNSET
        else:
            web_generated_date = isoparse(_web_generated_date)

        _closure_date = d.pop("closureDate", UNSET)
        closure_date: datetime.date | Unset
        if isinstance(_closure_date, Unset):
            closure_date = UNSET
        else:
            closure_date = isoparse(_closure_date).date()

        address = d.pop("address", UNSET)

        display_address = d.pop("displayAddress", UNSET)

        eli = d.pop("ELI", UNSET)

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

        prints_considered_jointly = cast(list[str], d.pop("printsConsideredJointly", UNSET))

        process_header = cls(
            u_e=u_e,
            e_li=e_li,
            term=term,
            number=number,
            title=title,
            title_final=title_final,
            description=description,
            ue=ue,
            document_date=document_date,
            process_start_date=process_start_date,
            change_date=change_date,
            document_type=document_type,
            document_type_enum=document_type_enum,
            comments=comments,
            web_generated_date=web_generated_date,
            closure_date=closure_date,
            address=address,
            display_address=display_address,
            eli=eli,
            passed=passed,
            links=links,
            shorten_procedure=shorten_procedure,
            urgency_status=urgency_status,
            urgency_withdraw_date=urgency_withdraw_date,
            prints_considered_jointly=prints_considered_jointly,
        )

        process_header.additional_properties = d
        return process_header

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
