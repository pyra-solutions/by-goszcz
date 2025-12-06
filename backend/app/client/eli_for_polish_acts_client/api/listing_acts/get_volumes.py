from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    publisher: str,
    year: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/acts/{publisher}/{year}/volumes".format(
            publisher=quote(str(publisher), safe=""),
            year=quote(str(year), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[int] | None:
    if response.status_code == 200:
        response_200 = cast(list[int], response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[list[int]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    publisher: str,
    year: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[list[int]]:
    """volumes

     returns a list of volumes for a given publisher and a given year

    Args:
        publisher (str):
        year (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[int]]
    """

    kwargs = _get_kwargs(
        publisher=publisher,
        year=year,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    publisher: str,
    year: int,
    *,
    client: AuthenticatedClient | Client,
) -> list[int] | None:
    """volumes

     returns a list of volumes for a given publisher and a given year

    Args:
        publisher (str):
        year (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[int]
    """

    return sync_detailed(
        publisher=publisher,
        year=year,
        client=client,
    ).parsed


async def asyncio_detailed(
    publisher: str,
    year: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[list[int]]:
    """volumes

     returns a list of volumes for a given publisher and a given year

    Args:
        publisher (str):
        year (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[int]]
    """

    kwargs = _get_kwargs(
        publisher=publisher,
        year=year,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    publisher: str,
    year: int,
    *,
    client: AuthenticatedClient | Client,
) -> list[int] | None:
    """volumes

     returns a list of volumes for a given publisher and a given year

    Args:
        publisher (str):
        year (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[int]
    """

    return (
        await asyncio_detailed(
            publisher=publisher,
            year=year,
            client=client,
        )
    ).parsed
