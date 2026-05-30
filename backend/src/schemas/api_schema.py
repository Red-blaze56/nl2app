"""
API Schema — endpoints, params, request/response shapes.
"""
from __future__ import annotations
from typing import Any, Literal
from pydantic import Field
from .base import BaseSchema
from .common import HTTPMethod, APIParamType


class APIParam(BaseSchema):
    name: str
    location: Literal["path", "query", "header"]
    type: APIParamType
    required: bool = True
    description: str = ""


class APIResponse(BaseSchema):
    status_code: int
    description: str
    schema_ref: str | None = None  # /components/schemas/ErrorResponse written as "ErrorResponse0". So claude dont have to generate more.


class APIEndpoint(BaseSchema):
    endpoint_id: str
    method: HTTPMethod
    path: str                           # e.g. /contacts/{id}
    summary: str
    tags: list[str] = Field(default_factory=list)
    auth_required: bool = True
    required_roles: list[str] = Field(default_factory=list)
    params: list[APIParam] = Field(default_factory=list)
    request_body_schema: str | None = None  # References a key in shared_schemas
    responses: list[APIResponse] = Field(default_factory=list)
    db_operations: list[str] = Field(
        default_factory=list,
        description="Tables touched: ['contacts:read', 'users:write']"
    )


class APISchema(BaseSchema):
    base_path: str = "/api/v1"
    endpoints: list[APIEndpoint]
    shared_schemas: dict[str, Any] = Field(
        default_factory=dict,
        description="Reusable request/response body schemas (JSON Schema format)"
    )