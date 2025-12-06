from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.committee import Committee
from ...types import Response


def _get_kwargs(
    term: int,
    code: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/sejm/term{term}/committees/{code}".format(
            term=quote(str(term), safe=""),
            code=quote(str(code), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Committee | None:
    if response.status_code == 200:
        response_200 = Committee.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Committee]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    term: int,
    code: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Committee]:
    """Returns a committee details

    Args:
        term (int):
        code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Committee]
    """

    kwargs = _get_kwargs(
        term=term,
        code=code,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    term: int,
    code: str,
    *,
    client: AuthenticatedClient | Client,
) -> Committee | None:
    """Returns a committee details

    Args:
        term (int):
        code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Committee
    """

    return sync_detailed(
        term=term,
        code=code,
        client=client,
    ).parsed


async def asyncio_detailed(
    term: int,
    code: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Committee]:
    """Returns a committee details

    Args:
        term (int):
        code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Committee]
    """

    kwargs = _get_kwargs(
        term=term,
        code=code,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    term: int,
    code: str,
    *,
    client: AuthenticatedClient | Client,
) -> Committee | None:
    """Returns a committee details

    Args:
        term (int):
        code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Committee
    """

    return (
        await asyncio_detailed(
            term=term,
            code=code,
            client=client,
        )
    ).parsed
