from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.club import Club
from ...types import Response


def _get_kwargs(
    term: int,
    id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/sejm/term{term}/clubs/{id}".format(
            term=quote(str(term), safe=""),
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Club | None:
    if response.status_code == 200:
        response_200 = Club.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Club]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    term: int,
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Club]:
    """Returns information about a club

    Args:
        term (int):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Club]
    """

    kwargs = _get_kwargs(
        term=term,
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    term: int,
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Club | None:
    """Returns information about a club

    Args:
        term (int):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Club
    """

    return sync_detailed(
        term=term,
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    term: int,
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Club]:
    """Returns information about a club

    Args:
        term (int):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Club]
    """

    kwargs = _get_kwargs(
        term=term,
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    term: int,
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Club | None:
    """Returns information about a club

    Args:
        term (int):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Club
    """

    return (
        await asyncio_detailed(
            term=term,
            id=id,
            client=client,
        )
    ).parsed
