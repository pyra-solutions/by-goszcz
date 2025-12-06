from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.print_ import Print
from ...types import UNSET, Response, Unset


def _get_kwargs(
    term: int,
    *,
    sort_by: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["sort_by"] = sort_by

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/sejm/term{term}/prints".format(
            term=quote(str(term), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[Print] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Print.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[list[Print]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    term: int,
    *,
    client: AuthenticatedClient | Client,
    sort_by: str | Unset = UNSET,
) -> Response[list[Print]]:
    """Returns a list of prints

    Args:
        term (int):
        sort_by (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[Print]]
    """

    kwargs = _get_kwargs(
        term=term,
        sort_by=sort_by,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    term: int,
    *,
    client: AuthenticatedClient | Client,
    sort_by: str | Unset = UNSET,
) -> list[Print] | None:
    """Returns a list of prints

    Args:
        term (int):
        sort_by (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[Print]
    """

    return sync_detailed(
        term=term,
        client=client,
        sort_by=sort_by,
    ).parsed


async def asyncio_detailed(
    term: int,
    *,
    client: AuthenticatedClient | Client,
    sort_by: str | Unset = UNSET,
) -> Response[list[Print]]:
    """Returns a list of prints

    Args:
        term (int):
        sort_by (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[Print]]
    """

    kwargs = _get_kwargs(
        term=term,
        sort_by=sort_by,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    term: int,
    *,
    client: AuthenticatedClient | Client,
    sort_by: str | Unset = UNSET,
) -> list[Print] | None:
    """Returns a list of prints

    Args:
        term (int):
        sort_by (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[Print]
    """

    return (
        await asyncio_detailed(
            term=term,
            client=client,
            sort_by=sort_by,
        )
    ).parsed
