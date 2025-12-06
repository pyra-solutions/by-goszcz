from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Video")


@_attrs_define
class Video:
    r"""a video

    Attributes:
        unid (str | Unset): An unique indentifier of a transmission Example: 758DAA6CDF68DFC0C12588F6003C6EF3.
        video_link (str | Unset): An URL or URLs to a video transmission Example:
            https://sejm.c.blueonline.tv/stream/ENC01/95D9F487F901760EC1258BA20052CC01/playlist.m3u8?start=1754380800000.
        other_video_links (list[str] | Unset): A list of URLs to a other cameras in a video transmission Example:
            https://sejm.c.blueonline.tv/stream/ENC30/95D9F487F901760EC1258BA20052CC01/playlist.m3u8?start=1754380800000.
        video_messages_link (str | Unset): A link to a messages for a transmission
        type_ (str | Unset): A type of transmission Example: komisja.
        transcribe (bool | Unset): Is there a transcription available Example: True.
        start_date_time (datetime.datetime | Unset): A start date and time of transmission Example: 2023-05-24 10:00:00.
        end_date_time (datetime.datetime | Unset): An end date and time of transmission Example: 2023-05-24 12:00:00.
        sign_lang_link (str | Unset): An URL of a sign language transmission
        title (str | Unset): A title of a transmission Example: Parlamentarny Zespół ds. Personelu Niemedycznego Ochrony
            Zdrowia.
        audio (str | Unset): A link to a an audio file
        room (str | Unset): A room where the transmission takes place Example: sala im. Konstytucji 3-go Maja (nr 118,
            bud. C).
        description (str | Unset): A description of a transmission Example: Medyczne zawody niemedyczne - przyszłość
            przenoszenia niektórych dodatkowych zadań w ramach opieki nad pacjentem na personel niemedyczny oraz tworzenie
            związanych z tym możliwości rozwoju zawodowego dla personelu.\r\n\r\n.
        committee (str | Unset): A committee code if the transmission is a committee meeting Example: SUE.
        subcommittee (str | Unset): A subcommittee code if the transmission is a subcommittee meeting Example: KSP02S.
        player_link (str | Unset): A link to a video player on the Sejm website
        player_link_i_frame (str | Unset): A link to a video player on the Sejm website, that can be embedded as iframe
    """

    unid: str | Unset = UNSET
    video_link: str | Unset = UNSET
    other_video_links: list[str] | Unset = UNSET
    video_messages_link: str | Unset = UNSET
    type_: str | Unset = UNSET
    transcribe: bool | Unset = UNSET
    start_date_time: datetime.datetime | Unset = UNSET
    end_date_time: datetime.datetime | Unset = UNSET
    sign_lang_link: str | Unset = UNSET
    title: str | Unset = UNSET
    audio: str | Unset = UNSET
    room: str | Unset = UNSET
    description: str | Unset = UNSET
    committee: str | Unset = UNSET
    subcommittee: str | Unset = UNSET
    player_link: str | Unset = UNSET
    player_link_i_frame: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unid = self.unid

        video_link = self.video_link

        other_video_links: list[str] | Unset = UNSET
        if not isinstance(self.other_video_links, Unset):
            other_video_links = self.other_video_links

        video_messages_link = self.video_messages_link

        type_ = self.type_

        transcribe = self.transcribe

        start_date_time: str | Unset = UNSET
        if not isinstance(self.start_date_time, Unset):
            start_date_time = self.start_date_time.isoformat()

        end_date_time: str | Unset = UNSET
        if not isinstance(self.end_date_time, Unset):
            end_date_time = self.end_date_time.isoformat()

        sign_lang_link = self.sign_lang_link

        title = self.title

        audio = self.audio

        room = self.room

        description = self.description

        committee = self.committee

        subcommittee = self.subcommittee

        player_link = self.player_link

        player_link_i_frame = self.player_link_i_frame

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if unid is not UNSET:
            field_dict["unid"] = unid
        if video_link is not UNSET:
            field_dict["videoLink"] = video_link
        if other_video_links is not UNSET:
            field_dict["otherVideoLinks"] = other_video_links
        if video_messages_link is not UNSET:
            field_dict["videoMessagesLink"] = video_messages_link
        if type_ is not UNSET:
            field_dict["type"] = type_
        if transcribe is not UNSET:
            field_dict["transcribe"] = transcribe
        if start_date_time is not UNSET:
            field_dict["startDateTime"] = start_date_time
        if end_date_time is not UNSET:
            field_dict["endDateTime"] = end_date_time
        if sign_lang_link is not UNSET:
            field_dict["signLangLink"] = sign_lang_link
        if title is not UNSET:
            field_dict["title"] = title
        if audio is not UNSET:
            field_dict["audio"] = audio
        if room is not UNSET:
            field_dict["room"] = room
        if description is not UNSET:
            field_dict["description"] = description
        if committee is not UNSET:
            field_dict["committee"] = committee
        if subcommittee is not UNSET:
            field_dict["subcommittee"] = subcommittee
        if player_link is not UNSET:
            field_dict["playerLink"] = player_link
        if player_link_i_frame is not UNSET:
            field_dict["playerLinkIFrame"] = player_link_i_frame

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        unid = d.pop("unid", UNSET)

        video_link = d.pop("videoLink", UNSET)

        other_video_links = cast(list[str], d.pop("otherVideoLinks", UNSET))

        video_messages_link = d.pop("videoMessagesLink", UNSET)

        type_ = d.pop("type", UNSET)

        transcribe = d.pop("transcribe", UNSET)

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

        sign_lang_link = d.pop("signLangLink", UNSET)

        title = d.pop("title", UNSET)

        audio = d.pop("audio", UNSET)

        room = d.pop("room", UNSET)

        description = d.pop("description", UNSET)

        committee = d.pop("committee", UNSET)

        subcommittee = d.pop("subcommittee", UNSET)

        player_link = d.pop("playerLink", UNSET)

        player_link_i_frame = d.pop("playerLinkIFrame", UNSET)

        video = cls(
            unid=unid,
            video_link=video_link,
            other_video_links=other_video_links,
            video_messages_link=video_messages_link,
            type_=type_,
            transcribe=transcribe,
            start_date_time=start_date_time,
            end_date_time=end_date_time,
            sign_lang_link=sign_lang_link,
            title=title,
            audio=audio,
            room=room,
            description=description,
            committee=committee,
            subcommittee=subcommittee,
            player_link=player_link,
            player_link_i_frame=player_link_i_frame,
        )

        video.additional_properties = d
        return video

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
