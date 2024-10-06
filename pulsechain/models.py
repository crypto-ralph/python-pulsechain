from pydantic import BaseModel
from typing import Any


class BaseResponse(BaseModel):
    items: list[dict[str, Any]]


class PaginatedResponse(BaseResponse):
    next_page_params: dict[str, Any] | None
