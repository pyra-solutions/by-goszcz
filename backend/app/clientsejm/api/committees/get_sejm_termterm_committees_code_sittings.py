from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.committee_sitting import CommitteeSitting
from ...types import UNSET, Response, Unset


def _get_kwargs(
    term: int,
    code: str,
    *,
    cancelled: bool | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["cancelled"] = cancelled

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/sejm/term{term}/committees/{code}/sittings".format(
            term=quote(str(term), safe=""),
            code=quote(str(code), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[CommitteeSitting] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = CommitteeSitting.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[CommitteeSitting]]:
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
    cancelled: bool | Unset = UNSET,
) -> Response[list[CommitteeSitting]]:
    """Returns a list of sittings

    Args:
        term (int):
        code (str):
        cancelled (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[CommitteeSitting]]
    """

    kwargs = _get_kwargs(
        term=term,
        code=code,
        cancelled=cancelled,
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
    cancelled: bool | Unset = UNSET,
) -> list[CommitteeSitting] | None:
    """Returns a list of sittings

    Args:
        term (int):
        code (str):
        cancelled (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[CommitteeSitting]
    """

    return sync_detailed(
        term=term,
        code=code,
        client=client,
        cancelled=cancelled,
    ).parsed


async def asyncio_detailed(
    term: int,
    code: str,
    *,
    client: AuthenticatedClient | Client,
    cancelled: bool | Unset = UNSET,
) -> Response[list[CommitteeSitting]]:
    """Returns a list of sittings

    Args:
        term (int):
        code (str):
        cancelled (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[CommitteeSitting]]
    """

    kwargs = _get_kwargs(
        term=term,
        code=code,
        cancelled=cancelled,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    term: int,
    code: str,
    *,
    client: AuthenticatedClient | Client,
    cancelled: bool | Unset = UNSET,
) -> list[CommitteeSitting] | None:
    """Returns a list of sittings

    Args:
        term (int):
        code (str):
        cancelled (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[CommitteeSitting]
    """

    return (
        await asyncio_detailed(
            term=term,
            code=code,
            client=client,
            cancelled=cancelled,
        )
    ).parsed
