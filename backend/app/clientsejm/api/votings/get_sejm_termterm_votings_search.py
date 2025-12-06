import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.voting import Voting
from ...types import UNSET, Response, Unset


def _get_kwargs(
    term: int,
    *,
    date_from: datetime.date | Unset = UNSET,
    date_to: datetime.date | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    proceeding: int | Unset = UNSET,
    title: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_date_from: str | Unset = UNSET
    if not isinstance(date_from, Unset):
        json_date_from = date_from.isoformat()
    params["dateFrom"] = json_date_from

    json_date_to: str | Unset = UNSET
    if not isinstance(date_to, Unset):
        json_date_to = date_to.isoformat()
    params["dateTo"] = json_date_to

    params["limit"] = limit

    params["offset"] = offset

    params["proceeding"] = proceeding

    params["title"] = title

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/sejm/term{term}/votings/search".format(
            term=quote(str(term), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[Voting] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Voting.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[list[Voting]]:
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
    date_from: datetime.date | Unset = UNSET,
    date_to: datetime.date | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    proceeding: int | Unset = UNSET,
    title: str | Unset = UNSET,
) -> Response[list[Voting]]:
    """Search for a voting

    Args:
        term (int):
        date_from (datetime.date | Unset):  Example: 2022-03-10.
        date_to (datetime.date | Unset):  Example: 2022-03-10.
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        proceeding (int | Unset):
        title (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[Voting]]
    """

    kwargs = _get_kwargs(
        term=term,
        date_from=date_from,
        date_to=date_to,
        limit=limit,
        offset=offset,
        proceeding=proceeding,
        title=title,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    term: int,
    *,
    client: AuthenticatedClient | Client,
    date_from: datetime.date | Unset = UNSET,
    date_to: datetime.date | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    proceeding: int | Unset = UNSET,
    title: str | Unset = UNSET,
) -> list[Voting] | None:
    """Search for a voting

    Args:
        term (int):
        date_from (datetime.date | Unset):  Example: 2022-03-10.
        date_to (datetime.date | Unset):  Example: 2022-03-10.
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        proceeding (int | Unset):
        title (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[Voting]
    """

    return sync_detailed(
        term=term,
        client=client,
        date_from=date_from,
        date_to=date_to,
        limit=limit,
        offset=offset,
        proceeding=proceeding,
        title=title,
    ).parsed


async def asyncio_detailed(
    term: int,
    *,
    client: AuthenticatedClient | Client,
    date_from: datetime.date | Unset = UNSET,
    date_to: datetime.date | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    proceeding: int | Unset = UNSET,
    title: str | Unset = UNSET,
) -> Response[list[Voting]]:
    """Search for a voting

    Args:
        term (int):
        date_from (datetime.date | Unset):  Example: 2022-03-10.
        date_to (datetime.date | Unset):  Example: 2022-03-10.
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        proceeding (int | Unset):
        title (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[Voting]]
    """

    kwargs = _get_kwargs(
        term=term,
        date_from=date_from,
        date_to=date_to,
        limit=limit,
        offset=offset,
        proceeding=proceeding,
        title=title,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    term: int,
    *,
    client: AuthenticatedClient | Client,
    date_from: datetime.date | Unset = UNSET,
    date_to: datetime.date | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    proceeding: int | Unset = UNSET,
    title: str | Unset = UNSET,
) -> list[Voting] | None:
    """Search for a voting

    Args:
        term (int):
        date_from (datetime.date | Unset):  Example: 2022-03-10.
        date_to (datetime.date | Unset):  Example: 2022-03-10.
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        proceeding (int | Unset):
        title (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[Voting]
    """

    return (
        await asyncio_detailed(
            term=term,
            client=client,
            date_from=date_from,
            date_to=date_to,
            limit=limit,
            offset=offset,
            proceeding=proceeding,
            title=title,
        )
    ).parsed
