from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.case_recipient_details import CaseRecipientDetails
    from ..models.reply import Reply


T = TypeVar("T", bound="WrittenQuestion")


@_attrs_define
class WrittenQuestion:
    """A written question (pl: zapytanie).

    Attributes:
        term (int | Unset): A Sejm term when the document was submitted Example: 9.
        num (int | Unset): A document number Example: 14710.
        title (str | Unset): A title of the case Example: Interpelacja w sprawie trudnej sytuacji osób niepełnosprawnych
            z uwagi na kwarantannę nakładaną na ich opiekunów.
        receipt_date (datetime.date | Unset): A date when the case was received Example: 2020-11-16.
        last_modified (datetime.datetime | Unset): A date of last modification of a document Example: 2022-09-07
            15:01:42.
        links (list[Any] | Unset): Links to HTML pages with a description or a content (body)
        from_ (list[str] | Unset): A list of IDs of MPs who submitted the question Example: 101.
        to (list[str] | Unset): A list of ministries to whom the question was sent Example: ['minister rodziny i
            polityki społecznej', 'minister zdrowia'].
        recipient_details (list[CaseRecipientDetails] | Unset): A more detailed list of ministries to whom the question
            was sent
        sent_date (datetime.date | Unset): A date when the interpellation was sent to recipients Example: 2021-01-20.
        replies (list[Reply] | Unset): A list of replies
        answer_delayed_days (int | Unset): number of days an answer is delayed for a given case. When there are multiple
            recipients then a maximum value is taken. Example: 300.
    """

    term: int | Unset = UNSET
    num: int | Unset = UNSET
    title: str | Unset = UNSET
    receipt_date: datetime.date | Unset = UNSET
    last_modified: datetime.datetime | Unset = UNSET
    links: list[Any] | Unset = UNSET
    from_: list[str] | Unset = UNSET
    to: list[str] | Unset = UNSET
    recipient_details: list[CaseRecipientDetails] | Unset = UNSET
    sent_date: datetime.date | Unset = UNSET
    replies: list[Reply] | Unset = UNSET
    answer_delayed_days: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        term = self.term

        num = self.num

        title = self.title

        receipt_date: str | Unset = UNSET
        if not isinstance(self.receipt_date, Unset):
            receipt_date = self.receipt_date.isoformat()

        last_modified: str | Unset = UNSET
        if not isinstance(self.last_modified, Unset):
            last_modified = self.last_modified.isoformat()

        links: list[Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links

        from_: list[str] | Unset = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_

        to: list[str] | Unset = UNSET
        if not isinstance(self.to, Unset):
            to = self.to

        recipient_details: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.recipient_details, Unset):
            recipient_details = []
            for recipient_details_item_data in self.recipient_details:
                recipient_details_item = recipient_details_item_data.to_dict()
                recipient_details.append(recipient_details_item)

        sent_date: str | Unset = UNSET
        if not isinstance(self.sent_date, Unset):
            sent_date = self.sent_date.isoformat()

        replies: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.replies, Unset):
            replies = []
            for replies_item_data in self.replies:
                replies_item = replies_item_data.to_dict()
                replies.append(replies_item)

        answer_delayed_days = self.answer_delayed_days

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if term is not UNSET:
            field_dict["term"] = term
        if num is not UNSET:
            field_dict["num"] = num
        if title is not UNSET:
            field_dict["title"] = title
        if receipt_date is not UNSET:
            field_dict["receiptDate"] = receipt_date
        if last_modified is not UNSET:
            field_dict["lastModified"] = last_modified
        if links is not UNSET:
            field_dict["links"] = links
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to
        if recipient_details is not UNSET:
            field_dict["recipientDetails"] = recipient_details
        if sent_date is not UNSET:
            field_dict["sentDate"] = sent_date
        if replies is not UNSET:
            field_dict["replies"] = replies
        if answer_delayed_days is not UNSET:
            field_dict["answerDelayedDays"] = answer_delayed_days

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.case_recipient_details import CaseRecipientDetails
        from ..models.reply import Reply

        d = dict(src_dict)
        term = d.pop("term", UNSET)

        num = d.pop("num", UNSET)

        title = d.pop("title", UNSET)

        _receipt_date = d.pop("receiptDate", UNSET)
        receipt_date: datetime.date | Unset
        if isinstance(_receipt_date, Unset):
            receipt_date = UNSET
        else:
            receipt_date = isoparse(_receipt_date).date()

        _last_modified = d.pop("lastModified", UNSET)
        last_modified: datetime.datetime | Unset
        if isinstance(_last_modified, Unset):
            last_modified = UNSET
        else:
            last_modified = isoparse(_last_modified)

        links = cast(list[Any], d.pop("links", UNSET))

        from_ = cast(list[str], d.pop("from", UNSET))

        to = cast(list[str], d.pop("to", UNSET))

        _recipient_details = d.pop("recipientDetails", UNSET)
        recipient_details: list[CaseRecipientDetails] | Unset = UNSET
        if _recipient_details is not UNSET:
            recipient_details = []
            for recipient_details_item_data in _recipient_details:
                recipient_details_item = CaseRecipientDetails.from_dict(recipient_details_item_data)

                recipient_details.append(recipient_details_item)

        _sent_date = d.pop("sentDate", UNSET)
        sent_date: datetime.date | Unset
        if isinstance(_sent_date, Unset):
            sent_date = UNSET
        else:
            sent_date = isoparse(_sent_date).date()

        _replies = d.pop("replies", UNSET)
        replies: list[Reply] | Unset = UNSET
        if _replies is not UNSET:
            replies = []
            for replies_item_data in _replies:
                replies_item = Reply.from_dict(replies_item_data)

                replies.append(replies_item)

        answer_delayed_days = d.pop("answerDelayedDays", UNSET)

        written_question = cls(
            term=term,
            num=num,
            title=title,
            receipt_date=receipt_date,
            last_modified=last_modified,
            links=links,
            from_=from_,
            to=to,
            recipient_details=recipient_details,
            sent_date=sent_date,
            replies=replies,
            answer_delayed_days=answer_delayed_days,
        )

        written_question.additional_properties = d
        return written_question

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
