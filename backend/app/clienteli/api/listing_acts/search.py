from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.acts import Acts
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    date: str | Unset = UNSET,
    date_effect: str | Unset = UNSET,
    date_effect_from: str | Unset = UNSET,
    date_effect_to: str | Unset = UNSET,
    date_from: str | Unset = UNSET,
    date_to: str | Unset = UNSET,
    exile: str | Unset = UNSET,
    in_force: str | Unset = UNSET,
    keyword: str | Unset = UNSET,
    limit: int | Unset = 500,
    offset: int | Unset = 0,
    position: int | Unset = UNSET,
    pub_date: str | Unset = UNSET,
    pub_date_from: str | Unset = UNSET,
    pub_date_to: str | Unset = UNSET,
    publisher: str | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    sort_dir: str | Unset = UNSET,
    title: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    volume: int | Unset = UNSET,
    year: int | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["date"] = date

    params["dateEffect"] = date_effect

    params["dateEffectFrom"] = date_effect_from

    params["dateEffectTo"] = date_effect_to

    params["dateFrom"] = date_from

    params["dateTo"] = date_to

    params["exile"] = exile

    params["inForce"] = in_force

    params["keyword"] = keyword

    params["limit"] = limit

    params["offset"] = offset

    params["position"] = position

    params["pubDate"] = pub_date

    params["pubDateFrom"] = pub_date_from

    params["pubDateTo"] = pub_date_to

    params["publisher"] = publisher

    params["sortBy"] = sort_by

    params["sortDir"] = sort_dir

    params["title"] = title

    params["type"] = type_

    params["volume"] = volume

    params["year"] = year

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/acts/search",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Acts | None:
    if response.status_code == 200:
        response_200 = Acts.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Acts]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    date: str | Unset = UNSET,
    date_effect: str | Unset = UNSET,
    date_effect_from: str | Unset = UNSET,
    date_effect_to: str | Unset = UNSET,
    date_from: str | Unset = UNSET,
    date_to: str | Unset = UNSET,
    exile: str | Unset = UNSET,
    in_force: str | Unset = UNSET,
    keyword: str | Unset = UNSET,
    limit: int | Unset = 500,
    offset: int | Unset = 0,
    position: int | Unset = UNSET,
    pub_date: str | Unset = UNSET,
    pub_date_from: str | Unset = UNSET,
    pub_date_to: str | Unset = UNSET,
    publisher: str | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    sort_dir: str | Unset = UNSET,
    title: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    volume: int | Unset = UNSET,
    year: int | Unset = UNSET,
) -> Response[Acts]:
    """search for acts

     Finds acts that match a specified criteria.

    Args:
        date (str | Unset):
        date_effect (str | Unset):
        date_effect_from (str | Unset):
        date_effect_to (str | Unset):
        date_from (str | Unset):
        date_to (str | Unset):
        exile (str | Unset):
        in_force (str | Unset):
        keyword (str | Unset):
        limit (int | Unset):  Default: 500.
        offset (int | Unset):  Default: 0.
        position (int | Unset):
        pub_date (str | Unset):
        pub_date_from (str | Unset):
        pub_date_to (str | Unset):
        publisher (str | Unset):
        sort_by (str | Unset):
        sort_dir (str | Unset):
        title (str | Unset):
        type_ (str | Unset):
        volume (int | Unset):
        year (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Acts]
    """

    kwargs = _get_kwargs(
        date=date,
        date_effect=date_effect,
        date_effect_from=date_effect_from,
        date_effect_to=date_effect_to,
        date_from=date_from,
        date_to=date_to,
        exile=exile,
        in_force=in_force,
        keyword=keyword,
        limit=limit,
        offset=offset,
        position=position,
        pub_date=pub_date,
        pub_date_from=pub_date_from,
        pub_date_to=pub_date_to,
        publisher=publisher,
        sort_by=sort_by,
        sort_dir=sort_dir,
        title=title,
        type_=type_,
        volume=volume,
        year=year,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    date: str | Unset = UNSET,
    date_effect: str | Unset = UNSET,
    date_effect_from: str | Unset = UNSET,
    date_effect_to: str | Unset = UNSET,
    date_from: str | Unset = UNSET,
    date_to: str | Unset = UNSET,
    exile: str | Unset = UNSET,
    in_force: str | Unset = UNSET,
    keyword: str | Unset = UNSET,
    limit: int | Unset = 500,
    offset: int | Unset = 0,
    position: int | Unset = UNSET,
    pub_date: str | Unset = UNSET,
    pub_date_from: str | Unset = UNSET,
    pub_date_to: str | Unset = UNSET,
    publisher: str | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    sort_dir: str | Unset = UNSET,
    title: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    volume: int | Unset = UNSET,
    year: int | Unset = UNSET,
) -> Acts | None:
    """search for acts

     Finds acts that match a specified criteria.

    Args:
        date (str | Unset):
        date_effect (str | Unset):
        date_effect_from (str | Unset):
        date_effect_to (str | Unset):
        date_from (str | Unset):
        date_to (str | Unset):
        exile (str | Unset):
        in_force (str | Unset):
        keyword (str | Unset):
        limit (int | Unset):  Default: 500.
        offset (int | Unset):  Default: 0.
        position (int | Unset):
        pub_date (str | Unset):
        pub_date_from (str | Unset):
        pub_date_to (str | Unset):
        publisher (str | Unset):
        sort_by (str | Unset):
        sort_dir (str | Unset):
        title (str | Unset):
        type_ (str | Unset):
        volume (int | Unset):
        year (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Acts
    """

    return sync_detailed(
        client=client,
        date=date,
        date_effect=date_effect,
        date_effect_from=date_effect_from,
        date_effect_to=date_effect_to,
        date_from=date_from,
        date_to=date_to,
        exile=exile,
        in_force=in_force,
        keyword=keyword,
        limit=limit,
        offset=offset,
        position=position,
        pub_date=pub_date,
        pub_date_from=pub_date_from,
        pub_date_to=pub_date_to,
        publisher=publisher,
        sort_by=sort_by,
        sort_dir=sort_dir,
        title=title,
        type_=type_,
        volume=volume,
        year=year,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    date: str | Unset = UNSET,
    date_effect: str | Unset = UNSET,
    date_effect_from: str | Unset = UNSET,
    date_effect_to: str | Unset = UNSET,
    date_from: str | Unset = UNSET,
    date_to: str | Unset = UNSET,
    exile: str | Unset = UNSET,
    in_force: str | Unset = UNSET,
    keyword: str | Unset = UNSET,
    limit: int | Unset = 500,
    offset: int | Unset = 0,
    position: int | Unset = UNSET,
    pub_date: str | Unset = UNSET,
    pub_date_from: str | Unset = UNSET,
    pub_date_to: str | Unset = UNSET,
    publisher: str | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    sort_dir: str | Unset = UNSET,
    title: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    volume: int | Unset = UNSET,
    year: int | Unset = UNSET,
) -> Response[Acts]:
    """search for acts

     Finds acts that match a specified criteria.

    Args:
        date (str | Unset):
        date_effect (str | Unset):
        date_effect_from (str | Unset):
        date_effect_to (str | Unset):
        date_from (str | Unset):
        date_to (str | Unset):
        exile (str | Unset):
        in_force (str | Unset):
        keyword (str | Unset):
        limit (int | Unset):  Default: 500.
        offset (int | Unset):  Default: 0.
        position (int | Unset):
        pub_date (str | Unset):
        pub_date_from (str | Unset):
        pub_date_to (str | Unset):
        publisher (str | Unset):
        sort_by (str | Unset):
        sort_dir (str | Unset):
        title (str | Unset):
        type_ (str | Unset):
        volume (int | Unset):
        year (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Acts]
    """

    kwargs = _get_kwargs(
        date=date,
        date_effect=date_effect,
        date_effect_from=date_effect_from,
        date_effect_to=date_effect_to,
        date_from=date_from,
        date_to=date_to,
        exile=exile,
        in_force=in_force,
        keyword=keyword,
        limit=limit,
        offset=offset,
        position=position,
        pub_date=pub_date,
        pub_date_from=pub_date_from,
        pub_date_to=pub_date_to,
        publisher=publisher,
        sort_by=sort_by,
        sort_dir=sort_dir,
        title=title,
        type_=type_,
        volume=volume,
        year=year,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    date: str | Unset = UNSET,
    date_effect: str | Unset = UNSET,
    date_effect_from: str | Unset = UNSET,
    date_effect_to: str | Unset = UNSET,
    date_from: str | Unset = UNSET,
    date_to: str | Unset = UNSET,
    exile: str | Unset = UNSET,
    in_force: str | Unset = UNSET,
    keyword: str | Unset = UNSET,
    limit: int | Unset = 500,
    offset: int | Unset = 0,
    position: int | Unset = UNSET,
    pub_date: str | Unset = UNSET,
    pub_date_from: str | Unset = UNSET,
    pub_date_to: str | Unset = UNSET,
    publisher: str | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    sort_dir: str | Unset = UNSET,
    title: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    volume: int | Unset = UNSET,
    year: int | Unset = UNSET,
) -> Acts | None:
    """search for acts

     Finds acts that match a specified criteria.

    Args:
        date (str | Unset):
        date_effect (str | Unset):
        date_effect_from (str | Unset):
        date_effect_to (str | Unset):
        date_from (str | Unset):
        date_to (str | Unset):
        exile (str | Unset):
        in_force (str | Unset):
        keyword (str | Unset):
        limit (int | Unset):  Default: 500.
        offset (int | Unset):  Default: 0.
        position (int | Unset):
        pub_date (str | Unset):
        pub_date_from (str | Unset):
        pub_date_to (str | Unset):
        publisher (str | Unset):
        sort_by (str | Unset):
        sort_dir (str | Unset):
        title (str | Unset):
        type_ (str | Unset):
        volume (int | Unset):
        year (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Acts
    """

    return (
        await asyncio_detailed(
            client=client,
            date=date,
            date_effect=date_effect,
            date_effect_from=date_effect_from,
            date_effect_to=date_effect_to,
            date_from=date_from,
            date_to=date_to,
            exile=exile,
            in_force=in_force,
            keyword=keyword,
            limit=limit,
            offset=offset,
            position=position,
            pub_date=pub_date,
            pub_date_from=pub_date_from,
            pub_date_to=pub_date_to,
            publisher=publisher,
            sort_by=sort_by,
            sort_dir=sort_dir,
            title=title,
            type_=type_,
            volume=volume,
            year=year,
        )
    ).parsed
