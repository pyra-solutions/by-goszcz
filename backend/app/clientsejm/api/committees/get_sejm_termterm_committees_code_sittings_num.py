from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.committee_sitting import CommitteeSitting
from ...types import Response


def _get_kwargs(
    term: int,
    code: str,
    num: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/sejm/term{term}/committees/{code}/sittings/{num}".format(
            term=quote(str(term), safe=""),
            code=quote(str(code), safe=""),
            num=quote(str(num), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CommitteeSitting | None:
    if response.status_code == 200:
        response_200 = CommitteeSitting.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CommitteeSitting]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    term: int,
    code: str,
    num: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[CommitteeSitting]:
    """Returns details about a sitting

    Args:
        term (int):
        code (str):
        num (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CommitteeSitting]
    """

    kwargs = _get_kwargs(
        term=term,
        code=code,
        num=num,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    term: int,
    code: str,
    num: int,
    *,
    client: AuthenticatedClient | Client,
) -> CommitteeSitting | None:
    """Returns details about a sitting

    Args:
        term (int):
        code (str):
        num (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CommitteeSitting
    """

    return sync_detailed(
        term=term,
        code=code,
        num=num,
        client=client,
    ).parsed


async def asyncio_detailed(
    term: int,
    code: str,
    num: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[CommitteeSitting]:
    """Returns details about a sitting

    Args:
        term (int):
        code (str):
        num (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CommitteeSitting]
    """

    kwargs = _get_kwargs(
        term=term,
        code=code,
        num=num,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    term: int,
    code: str,
    num: int,
    *,
    client: AuthenticatedClient | Client,
) -> CommitteeSitting | None:
    """Returns details about a sitting

    Args:
        term (int):
        code (str):
        num (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CommitteeSitting
    """

    return (
        await asyncio_detailed(
            term=term,
            code=code,
            num=num,
            client=client,
        )
    ).parsed
