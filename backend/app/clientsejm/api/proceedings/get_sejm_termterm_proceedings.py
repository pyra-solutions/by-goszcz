from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.proceeding import Proceeding
from ...types import Response


def _get_kwargs(
    term: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/sejm/term{term}/proceedings".format(
            term=quote(str(term), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[Proceeding] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Proceeding.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[list[Proceeding]]:
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
) -> Response[list[Proceeding]]:
    """Returns a list of proceedings

    Args:
        term (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[Proceeding]]
    """

    kwargs = _get_kwargs(
        term=term,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    term: int,
    *,
    client: AuthenticatedClient | Client,
) -> list[Proceeding] | None:
    """Returns a list of proceedings

    Args:
        term (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[Proceeding]
    """

    return sync_detailed(
        term=term,
        client=client,
    ).parsed


async def asyncio_detailed(
    term: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[list[Proceeding]]:
    """Returns a list of proceedings

    Args:
        term (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[Proceeding]]
    """

    kwargs = _get_kwargs(
        term=term,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    term: int,
    *,
    client: AuthenticatedClient | Client,
) -> list[Proceeding] | None:
    """Returns a list of proceedings

    Args:
        term (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[Proceeding]
    """

    return (
        await asyncio_detailed(
            term=term,
            client=client,
        )
    ).parsed
