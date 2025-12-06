from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.acts import Acts
from ...types import Response


def _get_kwargs(
    publisher: str,
    year: int,
    volume: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/acts/{publisher}/{year}/volumes/{volume}".format(
            publisher=quote(str(publisher), safe=""),
            year=quote(str(year), safe=""),
            volume=quote(str(volume), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Acts | Any | None:
    if response.status_code == 200:
        response_200 = Acts.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Acts | Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    publisher: str,
    year: int,
    volume: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Acts | Any]:
    """acts in volume

     returns a list of acts for a given volume

    Args:
        publisher (str):
        year (int):
        volume (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Acts | Any]
    """

    kwargs = _get_kwargs(
        publisher=publisher,
        year=year,
        volume=volume,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    publisher: str,
    year: int,
    volume: int,
    *,
    client: AuthenticatedClient | Client,
) -> Acts | Any | None:
    """acts in volume

     returns a list of acts for a given volume

    Args:
        publisher (str):
        year (int):
        volume (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Acts | Any
    """

    return sync_detailed(
        publisher=publisher,
        year=year,
        volume=volume,
        client=client,
    ).parsed


async def asyncio_detailed(
    publisher: str,
    year: int,
    volume: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Acts | Any]:
    """acts in volume

     returns a list of acts for a given volume

    Args:
        publisher (str):
        year (int):
        volume (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Acts | Any]
    """

    kwargs = _get_kwargs(
        publisher=publisher,
        year=year,
        volume=volume,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    publisher: str,
    year: int,
    volume: int,
    *,
    client: AuthenticatedClient | Client,
) -> Acts | Any | None:
    """acts in volume

     returns a list of acts for a given volume

    Args:
        publisher (str):
        year (int):
        volume (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Acts | Any
    """

    return (
        await asyncio_detailed(
            publisher=publisher,
            year=year,
            volume=volume,
            client=client,
        )
    ).parsed
