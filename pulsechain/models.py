from typing import Any

from pydantic import BaseModel


class BaseResponse(BaseModel):
    items: list[dict[str, Any]]


class PaginatedResponse(BaseResponse):
    next_page_params: dict[str, Any] | None
