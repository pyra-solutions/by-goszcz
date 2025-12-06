from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.acts import Acts
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    since: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    params["since"] = since

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/changes/acts",
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
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    since: str,
) -> Response[Acts]:
    """changed acts

     Returns a list of changed acts, sorted by the change date.

    Args:
        limit (int | Unset):  Default: 100.
        offset (int | Unset):  Default: 0.
        since (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Acts]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        since=since,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    since: str,
) -> Acts | None:
    """changed acts

     Returns a list of changed acts, sorted by the change date.

    Args:
        limit (int | Unset):  Default: 100.
        offset (int | Unset):  Default: 0.
        since (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Acts
    """

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
        since=since,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    since: str,
) -> Response[Acts]:
    """changed acts

     Returns a list of changed acts, sorted by the change date.

    Args:
        limit (int | Unset):  Default: 100.
        offset (int | Unset):  Default: 0.
        since (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Acts]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        since=since,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    since: str,
) -> Acts | None:
    """changed acts

     Returns a list of changed acts, sorted by the change date.

    Args:
        limit (int | Unset):  Default: 100.
        offset (int | Unset):  Default: 0.
        since (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Acts
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
            since=since,
        )
    ).parsed
