from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.video import Video
from ...types import UNSET, Response, Unset


def _get_kwargs(
    term: int,
    *,
    comm: str | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    since: str | Unset = UNSET,
    till: str | Unset = UNSET,
    title: str | Unset = UNSET,
    type_: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["comm"] = comm

    params["limit"] = limit

    params["offset"] = offset

    params["since"] = since

    params["till"] = till

    params["title"] = title

    params["type"] = type_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/sejm/term{term}/videos".format(
            term=quote(str(term), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[Video] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Video.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[list[Video]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    term: int,
    *,
    client: AuthenticatedClient | Client,
    comm: str | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    since: str | Unset = UNSET,
    till: str | Unset = UNSET,
    title: str | Unset = UNSET,
    type_: str | Unset = UNSET,
) -> Response[list[Video]]:
    """Returns a list of video transmissions

    Args:
        term (int):
        comm (str | Unset):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        since (str | Unset):
        till (str | Unset):
        title (str | Unset):
        type_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[Video]]
    """

    kwargs = _get_kwargs(
        term=term,
        comm=comm,
        limit=limit,
        offset=offset,
        since=since,
        till=till,
        title=title,
        type_=type_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    term: int,
    *,
    client: AuthenticatedClient | Client,
    comm: str | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    since: str | Unset = UNSET,
    till: str | Unset = UNSET,
    title: str | Unset = UNSET,
    type_: str | Unset = UNSET,
) -> list[Video] | None:
    """Returns a list of video transmissions

    Args:
        term (int):
        comm (str | Unset):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        since (str | Unset):
        till (str | Unset):
        title (str | Unset):
        type_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[Video]
    """

    return sync_detailed(
        term=term,
        client=client,
        comm=comm,
        limit=limit,
        offset=offset,
        since=since,
        till=till,
        title=title,
        type_=type_,
    ).parsed


async def asyncio_detailed(
    term: int,
    *,
    client: AuthenticatedClient | Client,
    comm: str | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    since: str | Unset = UNSET,
    till: str | Unset = UNSET,
    title: str | Unset = UNSET,
    type_: str | Unset = UNSET,
) -> Response[list[Video]]:
    """Returns a list of video transmissions

    Args:
        term (int):
        comm (str | Unset):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        since (str | Unset):
        till (str | Unset):
        title (str | Unset):
        type_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[Video]]
    """

    kwargs = _get_kwargs(
        term=term,
        comm=comm,
        limit=limit,
        offset=offset,
        since=since,
        till=till,
        title=title,
        type_=type_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    term: int,
    *,
    client: AuthenticatedClient | Client,
    comm: str | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    since: str | Unset = UNSET,
    till: str | Unset = UNSET,
    title: str | Unset = UNSET,
    type_: str | Unset = UNSET,
) -> list[Video] | None:
    """Returns a list of video transmissions

    Args:
        term (int):
        comm (str | Unset):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        since (str | Unset):
        till (str | Unset):
        title (str | Unset):
        type_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[Video]
    """

    return (
        await asyncio_detailed(
            term=term,
            client=client,
            comm=comm,
            limit=limit,
            offset=offset,
            since=since,
            till=till,
            title=title,
            type_=type_,
        )
    ).parsed
