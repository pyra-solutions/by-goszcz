from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.sitting_status import SittingStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.committee_sitting_num import CommitteeSittingNum
    from ..models.video import Video


T = TypeVar("T", bound="CommitteeSitting")


@_attrs_define
class CommitteeSitting:
    """A committee sitting.

    Attributes:
        code (str | Unset): A committee code Example: ASW.
        num (int | Unset): A sitting number Example: 1.
        date (datetime.date | Unset): A sitting date Example: 2023-11-21.
        start_date_time (datetime.datetime | Unset): A sitting start date Example: 2023-11-21 10:00:00.
        end_date_time (datetime.datetime | Unset): A sitting end date Example: 2023-11-21 11:00:00.
        closed (bool | Unset): A flag indicating that a meeting is closed
        remote (bool | Unset): A flag indicating that a meeting is a remote meeting
        video (list[Video] | Unset): A list of video transmissions
        audio (str | Unset): A link to an audio file
        city (str | Unset): A city where meeting took place
        room (str | Unset): A room where the sitting takes place Example: sala im. Konstytucji 3-go Maja (nr 118, bud.
            C).
        notes (str | Unset): Additional notes Example: Posiedzenie Komisji zostało zwołane w trybie art. 152 ust. 2
            regulaminu Sejmu RP na wniosek grupy posłów przekazany do Komisji w dniu 12 czerwca 2025 r..
        comments (str | Unset): Additional comments Example: Nastąpiła zmiana porządku posiedzenia.
        joint_with (list[CommitteeSittingNum] | Unset): A list of committees at joint meeting
        agenda (str | Unset): An agenda of a meeting
        status (SittingStatus | Unset):
    """

    code: str | Unset = UNSET
    num: int | Unset = UNSET
    date: datetime.date | Unset = UNSET
    start_date_time: datetime.datetime | Unset = UNSET
    end_date_time: datetime.datetime | Unset = UNSET
    closed: bool | Unset = UNSET
    remote: bool | Unset = UNSET
    video: list[Video] | Unset = UNSET
    audio: str | Unset = UNSET
    city: str | Unset = UNSET
    room: str | Unset = UNSET
    notes: str | Unset = UNSET
    comments: str | Unset = UNSET
    joint_with: list[CommitteeSittingNum] | Unset = UNSET
    agenda: str | Unset = UNSET
    status: SittingStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        num = self.num

        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        start_date_time: str | Unset = UNSET
        if not isinstance(self.start_date_time, Unset):
            start_date_time = self.start_date_time.isoformat()

        end_date_time: str | Unset = UNSET
        if not isinstance(self.end_date_time, Unset):
            end_date_time = self.end_date_time.isoformat()

        closed = self.closed

        remote = self.remote

        video: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.video, Unset):
            video = []
            for video_item_data in self.video:
                video_item = video_item_data.to_dict()
                video.append(video_item)

        audio = self.audio

        city = self.city

        room = self.room

        notes = self.notes

        comments = self.comments

        joint_with: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.joint_with, Unset):
            joint_with = []
            for joint_with_item_data in self.joint_with:
                joint_with_item = joint_with_item_data.to_dict()
                joint_with.append(joint_with_item)

        agenda = self.agenda

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if num is not UNSET:
            field_dict["num"] = num
        if date is not UNSET:
            field_dict["date"] = date
        if start_date_time is not UNSET:
            field_dict["startDateTime"] = start_date_time
        if end_date_time is not UNSET:
            field_dict["endDateTime"] = end_date_time
        if closed is not UNSET:
            field_dict["closed"] = closed
        if remote is not UNSET:
            field_dict["remote"] = remote
        if video is not UNSET:
            field_dict["video"] = video
        if audio is not UNSET:
            field_dict["audio"] = audio
        if city is not UNSET:
            field_dict["city"] = city
        if room is not UNSET:
            field_dict["room"] = room
        if notes is not UNSET:
            field_dict["notes"] = notes
        if comments is not UNSET:
            field_dict["comments"] = comments
        if joint_with is not UNSET:
            field_dict["jointWith"] = joint_with
        if agenda is not UNSET:
            field_dict["agenda"] = agenda
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.committee_sitting_num import CommitteeSittingNum
        from ..models.video import Video

        d = dict(src_dict)
        code = d.pop("code", UNSET)

        num = d.pop("num", UNSET)

        _date = d.pop("date", UNSET)
        date: datetime.date | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()

        _start_date_time = d.pop("startDateTime", UNSET)
        start_date_time: datetime.datetime | Unset
        if isinstance(_start_date_time, Unset):
            start_date_time = UNSET
        else:
            start_date_time = isoparse(_start_date_time)

        _end_date_time = d.pop("endDateTime", UNSET)
        end_date_time: datetime.datetime | Unset
        if isinstance(_end_date_time, Unset):
            end_date_time = UNSET
        else:
            end_date_time = isoparse(_end_date_time)

        closed = d.pop("closed", UNSET)

        remote = d.pop("remote", UNSET)

        _video = d.pop("video", UNSET)
        video: list[Video] | Unset = UNSET
        if _video is not UNSET:
            video = []
            for video_item_data in _video:
                video_item = Video.from_dict(video_item_data)

                video.append(video_item)

        audio = d.pop("audio", UNSET)

        city = d.pop("city", UNSET)

        room = d.pop("room", UNSET)

        notes = d.pop("notes", UNSET)

        comments = d.pop("comments", UNSET)

        _joint_with = d.pop("jointWith", UNSET)
        joint_with: list[CommitteeSittingNum] | Unset = UNSET
        if _joint_with is not UNSET:
            joint_with = []
            for joint_with_item_data in _joint_with:
                joint_with_item = CommitteeSittingNum.from_dict(joint_with_item_data)

                joint_with.append(joint_with_item)

        agenda = d.pop("agenda", UNSET)

        _status = d.pop("status", UNSET)
        status: SittingStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SittingStatus(_status)

        committee_sitting = cls(
            code=code,
            num=num,
            date=date,
            start_date_time=start_date_time,
            end_date_time=end_date_time,
            closed=closed,
            remote=remote,
            video=video,
            audio=audio,
            city=city,
            room=room,
            notes=notes,
            comments=comments,
            joint_with=joint_with,
            agenda=agenda,
            status=status,
        )

        committee_sitting.additional_properties = d
        return committee_sitting

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
