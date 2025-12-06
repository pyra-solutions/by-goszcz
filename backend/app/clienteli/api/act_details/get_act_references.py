from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.references_details_info import ReferencesDetailsInfo
from ...types import Response


def _get_kwargs(
    publisher: str,
    year: int,
    position: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/acts/{publisher}/{year}/{position}/references".format(
            publisher=quote(str(publisher), safe=""),
            year=quote(str(year), safe=""),
            position=quote(str(position), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ReferencesDetailsInfo | None:
    if response.status_code == 200:
        response_200 = ReferencesDetailsInfo.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ReferencesDetailsInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    publisher: str,
    year: int,
    position: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | ReferencesDetailsInfo]:
    """act references

     Returns a map of type -> list of references for a given act

    Args:
        publisher (str):
        year (int):
        position (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ReferencesDetailsInfo]
    """

    kwargs = _get_kwargs(
        publisher=publisher,
        year=year,
        position=position,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    publisher: str,
    year: int,
    position: int,
    *,
    client: AuthenticatedClient | Client,
) -> Any | ReferencesDetailsInfo | None:
    """act references

     Returns a map of type -> list of references for a given act

    Args:
        publisher (str):
        year (int):
        position (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ReferencesDetailsInfo
    """

    return sync_detailed(
        publisher=publisher,
        year=year,
        position=position,
        client=client,
    ).parsed


async def asyncio_detailed(
    publisher: str,
    year: int,
    position: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | ReferencesDetailsInfo]:
    """act references

     Returns a map of type -> list of references for a given act

    Args:
        publisher (str):
        year (int):
        position (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ReferencesDetailsInfo]
    """

    kwargs = _get_kwargs(
        publisher=publisher,
        year=year,
        position=position,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    publisher: str,
    year: int,
    position: int,
    *,
    client: AuthenticatedClient | Client,
) -> Any | ReferencesDetailsInfo | None:
    """act references

     Returns a map of type -> list of references for a given act

    Args:
        publisher (str):
        year (int):
        position (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ReferencesDetailsInfo
    """

    return (
        await asyncio_detailed(
            publisher=publisher,
            year=year,
            position=position,
            client=client,
        )
    ).parsed
