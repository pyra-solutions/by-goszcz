from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.video import Video
from ...types import Response


def _get_kwargs(
    term: int,
    unid: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/sejm/term{term}/videos/{unid}".format(
            term=quote(str(term), safe=""),
            unid=quote(str(unid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Video | None:
    if response.status_code == 200:
        response_200 = Video.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Video]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    term: int,
    unid: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Video]:
    """Returns a video transmission details

    Args:
        term (int):
        unid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Video]
    """

    kwargs = _get_kwargs(
        term=term,
        unid=unid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    term: int,
    unid: str,
    *,
    client: AuthenticatedClient | Client,
) -> Video | None:
    """Returns a video transmission details

    Args:
        term (int):
        unid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Video
    """

    return sync_detailed(
        term=term,
        unid=unid,
        client=client,
    ).parsed


async def asyncio_detailed(
    term: int,
    unid: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Video]:
    """Returns a video transmission details

    Args:
        term (int):
        unid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Video]
    """

    kwargs = _get_kwargs(
        term=term,
        unid=unid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    term: int,
    unid: str,
    *,
    client: AuthenticatedClient | Client,
) -> Video | None:
    """Returns a video transmission details

    Args:
        term (int):
        unid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Video
    """

    return (
        await asyncio_detailed(
            term=term,
            unid=unid,
            client=client,
        )
    ).parsed
