import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.process_header import ProcessHeader
from ...types import UNSET, Response, Unset


def _get_kwargs(
    term: int,
    *,
    document_type: str | Unset = UNSET,
    limit: int | Unset = 50,
    modified_since: datetime.datetime | Unset = UNSET,
    offset: int | Unset = 0,
    passed: bool | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    title: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["documentType"] = document_type

    params["limit"] = limit

    json_modified_since: str | Unset = UNSET
    if not isinstance(modified_since, Unset):
        json_modified_since = modified_since.isoformat()
    params["modifiedSince"] = json_modified_since

    params["offset"] = offset

    params["passed"] = passed

    params["sort_by"] = sort_by

    params["title"] = title

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/sejm/term{term}/processes".format(
            term=quote(str(term), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[ProcessHeader] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ProcessHeader.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[list[ProcessHeader]]:
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
    document_type: str | Unset = UNSET,
    limit: int | Unset = 50,
    modified_since: datetime.datetime | Unset = UNSET,
    offset: int | Unset = 0,
    passed: bool | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    title: str | Unset = UNSET,
) -> Response[list[ProcessHeader]]:
    """Returns a list of legislative processes

    Args:
        term (int):
        document_type (str | Unset):
        limit (int | Unset):  Default: 50.
        modified_since (datetime.datetime | Unset):  Example: 2022-03-10 12:15:50.
        offset (int | Unset):  Default: 0.
        passed (bool | Unset):
        sort_by (str | Unset):
        title (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[ProcessHeader]]
    """

    kwargs = _get_kwargs(
        term=term,
        document_type=document_type,
        limit=limit,
        modified_since=modified_since,
        offset=offset,
        passed=passed,
        sort_by=sort_by,
        title=title,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    term: int,
    *,
    client: AuthenticatedClient | Client,
    document_type: str | Unset = UNSET,
    limit: int | Unset = 50,
    modified_since: datetime.datetime | Unset = UNSET,
    offset: int | Unset = 0,
    passed: bool | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    title: str | Unset = UNSET,
) -> list[ProcessHeader] | None:
    """Returns a list of legislative processes

    Args:
        term (int):
        document_type (str | Unset):
        limit (int | Unset):  Default: 50.
        modified_since (datetime.datetime | Unset):  Example: 2022-03-10 12:15:50.
        offset (int | Unset):  Default: 0.
        passed (bool | Unset):
        sort_by (str | Unset):
        title (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[ProcessHeader]
    """

    return sync_detailed(
        term=term,
        client=client,
        document_type=document_type,
        limit=limit,
        modified_since=modified_since,
        offset=offset,
        passed=passed,
        sort_by=sort_by,
        title=title,
    ).parsed


async def asyncio_detailed(
    term: int,
    *,
    client: AuthenticatedClient | Client,
    document_type: str | Unset = UNSET,
    limit: int | Unset = 50,
    modified_since: datetime.datetime | Unset = UNSET,
    offset: int | Unset = 0,
    passed: bool | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    title: str | Unset = UNSET,
) -> Response[list[ProcessHeader]]:
    """Returns a list of legislative processes

    Args:
        term (int):
        document_type (str | Unset):
        limit (int | Unset):  Default: 50.
        modified_since (datetime.datetime | Unset):  Example: 2022-03-10 12:15:50.
        offset (int | Unset):  Default: 0.
        passed (bool | Unset):
        sort_by (str | Unset):
        title (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[ProcessHeader]]
    """

    kwargs = _get_kwargs(
        term=term,
        document_type=document_type,
        limit=limit,
        modified_since=modified_since,
        offset=offset,
        passed=passed,
        sort_by=sort_by,
        title=title,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    term: int,
    *,
    client: AuthenticatedClient | Client,
    document_type: str | Unset = UNSET,
    limit: int | Unset = 50,
    modified_since: datetime.datetime | Unset = UNSET,
    offset: int | Unset = 0,
    passed: bool | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    title: str | Unset = UNSET,
) -> list[ProcessHeader] | None:
    """Returns a list of legislative processes

    Args:
        term (int):
        document_type (str | Unset):
        limit (int | Unset):  Default: 50.
        modified_since (datetime.datetime | Unset):  Example: 2022-03-10 12:15:50.
        offset (int | Unset):  Default: 0.
        passed (bool | Unset):
        sort_by (str | Unset):
        title (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[ProcessHeader]
    """

    return (
        await asyncio_detailed(
            term=term,
            client=client,
            document_type=document_type,
            limit=limit,
            modified_since=modified_since,
            offset=offset,
            passed=passed,
            sort_by=sort_by,
            title=title,
        )
    ).parsed
