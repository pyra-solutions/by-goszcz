from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.attachment import Attachment


T = TypeVar("T", bound="Reply")


@_attrs_define
class Reply:
    """reply to an interpellation or question

    Attributes:
        key (str | Unset): a reply identifier Example: BJWJSS.
        receipt_date (datetime.date | Unset): A date when the reply was received Example: 2021-01-29.
        last_modified (datetime.datetime | Unset): A date of last modification of a document Example: 2022-09-07
            15:01:42.
        from_ (str | Unset): A name of an author Example: Sekretarz stanu Waldemar Kraska.
        links (list[Any] | Unset): Links to HTML page with a description or a content (body)
        only_attachment (bool | Unset): Flag indicating that this reply contains only an attachment (without HTML body)
        attachments (list[Attachment] | Unset): Attachments
        prolongation (bool | Unset): Is this reply a prolongation. Text of prolongation is not published.
    """

    key: str | Unset = UNSET
    receipt_date: datetime.date | Unset = UNSET
    last_modified: datetime.datetime | Unset = UNSET
    from_: str | Unset = UNSET
    links: list[Any] | Unset = UNSET
    only_attachment: bool | Unset = UNSET
    attachments: list[Attachment] | Unset = UNSET
    prolongation: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        receipt_date: str | Unset = UNSET
        if not isinstance(self.receipt_date, Unset):
            receipt_date = self.receipt_date.isoformat()

        last_modified: str | Unset = UNSET
        if not isinstance(self.last_modified, Unset):
            last_modified = self.last_modified.isoformat()

        from_ = self.from_

        links: list[Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links

        only_attachment = self.only_attachment

        attachments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = []
            for attachments_item_data in self.attachments:
                attachments_item = attachments_item_data.to_dict()
                attachments.append(attachments_item)

        prolongation = self.prolongation

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if receipt_date is not UNSET:
            field_dict["receiptDate"] = receipt_date
        if last_modified is not UNSET:
            field_dict["lastModified"] = last_modified
        if from_ is not UNSET:
            field_dict["from"] = from_
        if links is not UNSET:
            field_dict["links"] = links
        if only_attachment is not UNSET:
            field_dict["onlyAttachment"] = only_attachment
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if prolongation is not UNSET:
            field_dict["prolongation"] = prolongation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.attachment import Attachment

        d = dict(src_dict)
        key = d.pop("key", UNSET)

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

        from_ = d.pop("from", UNSET)

        links = cast(list[Any], d.pop("links", UNSET))

        only_attachment = d.pop("onlyAttachment", UNSET)

        _attachments = d.pop("attachments", UNSET)
        attachments: list[Attachment] | Unset = UNSET
        if _attachments is not UNSET:
            attachments = []
            for attachments_item_data in _attachments:
                attachments_item = Attachment.from_dict(attachments_item_data)

                attachments.append(attachments_item)

        prolongation = d.pop("prolongation", UNSET)

        reply = cls(
            key=key,
            receipt_date=receipt_date,
            last_modified=last_modified,
            from_=from_,
            links=links,
            only_attachment=only_attachment,
            attachments=attachments,
            prolongation=prolongation,
        )

        reply.additional_properties = d
        return reply

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
