from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.act_info import ActInfo
    from ..models.act_query import ActQuery


T = TypeVar("T", bound="Acts")


@_attrs_define
class Acts:
    """A list of acts.

    Attributes:
        items (list[ActInfo] | Unset): a list of items
        offset (int | Unset): a starting offset
        count (int | Unset): a number of returned items Example: 20.
        total_count (int | Unset): total number of items Example: 23.
        search_query (ActQuery | Unset): a query for searching acts
    """

    items: list[ActInfo] | Unset = UNSET
    offset: int | Unset = UNSET
    count: int | Unset = UNSET
    total_count: int | Unset = UNSET
    search_query: ActQuery | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        offset = self.offset

        count = self.count

        total_count = self.total_count

        search_query: dict[str, Any] | Unset = UNSET
        if not isinstance(self.search_query, Unset):
            search_query = self.search_query.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if items is not UNSET:
            field_dict["items"] = items
        if offset is not UNSET:
            field_dict["offset"] = offset
        if count is not UNSET:
            field_dict["count"] = count
        if total_count is not UNSET:
            field_dict["totalCount"] = total_count
        if search_query is not UNSET:
            field_dict["searchQuery"] = search_query

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.act_info import ActInfo
        from ..models.act_query import ActQuery

        d = dict(src_dict)
        _items = d.pop("items", UNSET)
        items: list[ActInfo] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = ActInfo.from_dict(items_item_data)

                items.append(items_item)

        offset = d.pop("offset", UNSET)

        count = d.pop("count", UNSET)

        total_count = d.pop("totalCount", UNSET)

        _search_query = d.pop("searchQuery", UNSET)
        search_query: ActQuery | Unset
        if isinstance(_search_query, Unset):
            search_query = UNSET
        else:
            search_query = ActQuery.from_dict(_search_query)

        acts = cls(
            items=items,
            offset=offset,
            count=count,
            total_count=total_count,
            search_query=search_query,
        )

        acts.additional_properties = d
        return acts

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
