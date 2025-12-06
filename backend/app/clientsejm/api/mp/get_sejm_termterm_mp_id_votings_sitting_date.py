import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.vote_mp import VoteMP
from ...types import Response


def _get_kwargs(
    term: int,
    id: int,
    sitting: int,
    date: datetime.date,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/sejm/term{term}/MP/{id}/votings/{sitting}/{date}".format(
            term=quote(str(term), safe=""),
            id=quote(str(id), safe=""),
            sitting=quote(str(sitting), safe=""),
            date=quote(str(date), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[VoteMP] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = VoteMP.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[list[VoteMP]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    term: int,
    id: int,
    sitting: int,
    date: datetime.date,
    *,
    client: AuthenticatedClient | Client,
) -> Response[list[VoteMP]]:
    """Returns an information about votings for an MP

    Args:
        term (int):
        id (int):
        sitting (int):
        date (datetime.date):  Example: 2022-03-10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[VoteMP]]
    """

    kwargs = _get_kwargs(
        term=term,
        id=id,
        sitting=sitting,
        date=date,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    term: int,
    id: int,
    sitting: int,
    date: datetime.date,
    *,
    client: AuthenticatedClient | Client,
) -> list[VoteMP] | None:
    """Returns an information about votings for an MP

    Args:
        term (int):
        id (int):
        sitting (int):
        date (datetime.date):  Example: 2022-03-10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[VoteMP]
    """

    return sync_detailed(
        term=term,
        id=id,
        sitting=sitting,
        date=date,
        client=client,
    ).parsed


async def asyncio_detailed(
    term: int,
    id: int,
    sitting: int,
    date: datetime.date,
    *,
    client: AuthenticatedClient | Client,
) -> Response[list[VoteMP]]:
    """Returns an information about votings for an MP

    Args:
        term (int):
        id (int):
        sitting (int):
        date (datetime.date):  Example: 2022-03-10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[VoteMP]]
    """

    kwargs = _get_kwargs(
        term=term,
        id=id,
        sitting=sitting,
        date=date,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    term: int,
    id: int,
    sitting: int,
    date: datetime.date,
    *,
    client: AuthenticatedClient | Client,
) -> list[VoteMP] | None:
    """Returns an information about votings for an MP

    Args:
        term (int):
        id (int):
        sitting (int):
        date (datetime.date):  Example: 2022-03-10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[VoteMP]
    """

    return (
        await asyncio_detailed(
            term=term,
            id=id,
            sitting=sitting,
            date=date,
            client=client,
        )
    ).parsed
