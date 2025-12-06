import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    term: int,
    id: int,
    date: datetime.date,
    statement_num: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/sejm/term{term}/proceedings/{id}/{date}/transcripts/{statement_num}".format(
            term=quote(str(term), safe=""),
            id=quote(str(id), safe=""),
            date=quote(str(date), safe=""),
            statement_num=quote(str(statement_num), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 200:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    term: int,
    id: int,
    date: datetime.date,
    statement_num: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any]:
    """Returns a statement body in the HTML format

    Args:
        term (int):
        id (int):
        date (datetime.date):  Example: 2022-03-10.
        statement_num (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        term=term,
        id=id,
        date=date,
        statement_num=statement_num,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    term: int,
    id: int,
    date: datetime.date,
    statement_num: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any]:
    """Returns a statement body in the HTML format

    Args:
        term (int):
        id (int):
        date (datetime.date):  Example: 2022-03-10.
        statement_num (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        term=term,
        id=id,
        date=date,
        statement_num=statement_num,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
