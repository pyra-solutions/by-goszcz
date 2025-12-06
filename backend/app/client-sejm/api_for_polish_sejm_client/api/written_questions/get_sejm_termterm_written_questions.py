import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.written_question import WrittenQuestion
from ...types import UNSET, Response, Unset


def _get_kwargs(
    term: int,
    *,
    delayed: bool | Unset = UNSET,
    from_: str | Unset = UNSET,
    limit: int | Unset = 50,
    modified_since: datetime.datetime | Unset = UNSET,
    offset: int | Unset = 0,
    since: str | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    till: str | Unset = UNSET,
    title: str | Unset = UNSET,
    to: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["delayed"] = delayed

    params["from"] = from_

    params["limit"] = limit

    json_modified_since: str | Unset = UNSET
    if not isinstance(modified_since, Unset):
        json_modified_since = modified_since.isoformat()
    params["modifiedSince"] = json_modified_since

    params["offset"] = offset

    params["since"] = since

    params["sort_by"] = sort_by

    params["till"] = till

    params["title"] = title

    params["to"] = to

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/sejm/term{term}/writtenQuestions".format(
            term=quote(str(term), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[WrittenQuestion] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = WrittenQuestion.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[WrittenQuestion]]:
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
    delayed: bool | Unset = UNSET,
    from_: str | Unset = UNSET,
    limit: int | Unset = 50,
    modified_since: datetime.datetime | Unset = UNSET,
    offset: int | Unset = 0,
    since: str | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    till: str | Unset = UNSET,
    title: str | Unset = UNSET,
    to: str | Unset = UNSET,
) -> Response[list[WrittenQuestion]]:
    """Returns a list of written questions

    Args:
        term (int):
        delayed (bool | Unset):
        from_ (str | Unset):
        limit (int | Unset):  Default: 50.
        modified_since (datetime.datetime | Unset):  Example: 2022-03-10 12:15:50.
        offset (int | Unset):  Default: 0.
        since (str | Unset):
        sort_by (str | Unset):
        till (str | Unset):
        title (str | Unset):
        to (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[WrittenQuestion]]
    """

    kwargs = _get_kwargs(
        term=term,
        delayed=delayed,
        from_=from_,
        limit=limit,
        modified_since=modified_since,
        offset=offset,
        since=since,
        sort_by=sort_by,
        till=till,
        title=title,
        to=to,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    term: int,
    *,
    client: AuthenticatedClient | Client,
    delayed: bool | Unset = UNSET,
    from_: str | Unset = UNSET,
    limit: int | Unset = 50,
    modified_since: datetime.datetime | Unset = UNSET,
    offset: int | Unset = 0,
    since: str | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    till: str | Unset = UNSET,
    title: str | Unset = UNSET,
    to: str | Unset = UNSET,
) -> list[WrittenQuestion] | None:
    """Returns a list of written questions

    Args:
        term (int):
        delayed (bool | Unset):
        from_ (str | Unset):
        limit (int | Unset):  Default: 50.
        modified_since (datetime.datetime | Unset):  Example: 2022-03-10 12:15:50.
        offset (int | Unset):  Default: 0.
        since (str | Unset):
        sort_by (str | Unset):
        till (str | Unset):
        title (str | Unset):
        to (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[WrittenQuestion]
    """

    return sync_detailed(
        term=term,
        client=client,
        delayed=delayed,
        from_=from_,
        limit=limit,
        modified_since=modified_since,
        offset=offset,
        since=since,
        sort_by=sort_by,
        till=till,
        title=title,
        to=to,
    ).parsed


async def asyncio_detailed(
    term: int,
    *,
    client: AuthenticatedClient | Client,
    delayed: bool | Unset = UNSET,
    from_: str | Unset = UNSET,
    limit: int | Unset = 50,
    modified_since: datetime.datetime | Unset = UNSET,
    offset: int | Unset = 0,
    since: str | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    till: str | Unset = UNSET,
    title: str | Unset = UNSET,
    to: str | Unset = UNSET,
) -> Response[list[WrittenQuestion]]:
    """Returns a list of written questions

    Args:
        term (int):
        delayed (bool | Unset):
        from_ (str | Unset):
        limit (int | Unset):  Default: 50.
        modified_since (datetime.datetime | Unset):  Example: 2022-03-10 12:15:50.
        offset (int | Unset):  Default: 0.
        since (str | Unset):
        sort_by (str | Unset):
        till (str | Unset):
        title (str | Unset):
        to (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[WrittenQuestion]]
    """

    kwargs = _get_kwargs(
        term=term,
        delayed=delayed,
        from_=from_,
        limit=limit,
        modified_since=modified_since,
        offset=offset,
        since=since,
        sort_by=sort_by,
        till=till,
        title=title,
        to=to,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    term: int,
    *,
    client: AuthenticatedClient | Client,
    delayed: bool | Unset = UNSET,
    from_: str | Unset = UNSET,
    limit: int | Unset = 50,
    modified_since: datetime.datetime | Unset = UNSET,
    offset: int | Unset = 0,
    since: str | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    till: str | Unset = UNSET,
    title: str | Unset = UNSET,
    to: str | Unset = UNSET,
) -> list[WrittenQuestion] | None:
    """Returns a list of written questions

    Args:
        term (int):
        delayed (bool | Unset):
        from_ (str | Unset):
        limit (int | Unset):  Default: 50.
        modified_since (datetime.datetime | Unset):  Example: 2022-03-10 12:15:50.
        offset (int | Unset):  Default: 0.
        since (str | Unset):
        sort_by (str | Unset):
        till (str | Unset):
        title (str | Unset):
        to (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[WrittenQuestion]
    """

    return (
        await asyncio_detailed(
            term=term,
            client=client,
            delayed=delayed,
            from_=from_,
            limit=limit,
            modified_since=modified_since,
            offset=offset,
            since=since,
            sort_by=sort_by,
            till=till,
            title=title,
            to=to,
        )
    ).parsed
