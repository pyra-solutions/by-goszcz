from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.acts import Acts
from ...types import UNSET, Response, Unset


def _get_kwargs(
    publisher: str,
    year: int,
    *,
    sort_by: str | Unset = UNSET,
    sort_dir: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["sortBy"] = sort_by

    params["sortDir"] = sort_dir

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/acts/{publisher}/{year}".format(
            publisher=quote(str(publisher), safe=""),
            year=quote(str(year), safe=""),
        ),
        "params": params,
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
    *,
    client: AuthenticatedClient | Client,
    sort_by: str | Unset = UNSET,
    sort_dir: str | Unset = UNSET,
) -> Response[Acts | Any]:
    """acts in year

     Returns a list of acts for a given publisher and a given year

    Args:
        publisher (str):
        year (int):
        sort_by (str | Unset):
        sort_dir (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Acts | Any]
    """

    kwargs = _get_kwargs(
        publisher=publisher,
        year=year,
        sort_by=sort_by,
        sort_dir=sort_dir,
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
    sort_by: str | Unset = UNSET,
    sort_dir: str | Unset = UNSET,
) -> Acts | Any | None:
    """acts in year

     Returns a list of acts for a given publisher and a given year

    Args:
        publisher (str):
        year (int):
        sort_by (str | Unset):
        sort_dir (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Acts | Any
    """

    return sync_detailed(
        publisher=publisher,
        year=year,
        client=client,
        sort_by=sort_by,
        sort_dir=sort_dir,
    ).parsed


async def asyncio_detailed(
    publisher: str,
    year: int,
    *,
    client: AuthenticatedClient | Client,
    sort_by: str | Unset = UNSET,
    sort_dir: str | Unset = UNSET,
) -> Response[Acts | Any]:
    """acts in year

     Returns a list of acts for a given publisher and a given year

    Args:
        publisher (str):
        year (int):
        sort_by (str | Unset):
        sort_dir (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Acts | Any]
    """

    kwargs = _get_kwargs(
        publisher=publisher,
        year=year,
        sort_by=sort_by,
        sort_dir=sort_dir,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    publisher: str,
    year: int,
    *,
    client: AuthenticatedClient | Client,
    sort_by: str | Unset = UNSET,
    sort_dir: str | Unset = UNSET,
) -> Acts | Any | None:
    """acts in year

     Returns a list of acts for a given publisher and a given year

    Args:
        publisher (str):
        year (int):
        sort_by (str | Unset):
        sort_dir (str | Unset):

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
            client=client,
            sort_by=sort_by,
            sort_dir=sort_dir,
        )
    ).parsed
