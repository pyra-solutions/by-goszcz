from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.publishing_house import PublishingHouse
from ...types import Response


def _get_kwargs(
    publisher: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/acts/{publisher}".format(
            publisher=quote(str(publisher), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PublishingHouse | None:
    if response.status_code == 200:
        response_200 = PublishingHouse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PublishingHouse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    publisher: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[PublishingHouse]:
    """publisher info

     Returns an information about given publisher. The information about publisher contains a list of
    years in which there are any acts published.

    Args:
        publisher (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PublishingHouse]
    """

    kwargs = _get_kwargs(
        publisher=publisher,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    publisher: str,
    *,
    client: AuthenticatedClient | Client,
) -> PublishingHouse | None:
    """publisher info

     Returns an information about given publisher. The information about publisher contains a list of
    years in which there are any acts published.

    Args:
        publisher (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PublishingHouse
    """

    return sync_detailed(
        publisher=publisher,
        client=client,
    ).parsed


async def asyncio_detailed(
    publisher: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[PublishingHouse]:
    """publisher info

     Returns an information about given publisher. The information about publisher contains a list of
    years in which there are any acts published.

    Args:
        publisher (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PublishingHouse]
    """

    kwargs = _get_kwargs(
        publisher=publisher,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    publisher: str,
    *,
    client: AuthenticatedClient | Client,
) -> PublishingHouse | None:
    """publisher info

     Returns an information about given publisher. The information about publisher contains a list of
    years in which there are any acts published.

    Args:
        publisher (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PublishingHouse
    """

    return (
        await asyncio_detailed(
            publisher=publisher,
            client=client,
        )
    ).parsed
