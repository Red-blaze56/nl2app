"""
UI Schema — pages, components, fields.
"""
from __future__ import annotations
from typing import Literal
from pydantic import Field
from .base import BaseSchema
from .common import UIFieldType, HTTPMethod, PageType


class UIFieldValidation(BaseSchema):
    required: bool = False
    min_length: int | None = None
    max_length: int | None = None
    pattern: str | None = None
    min: float | None = None
    max: float | None = None


class UIField(BaseSchema):
    field_id: str = Field(..., description="Mirrors DB column / API payload key")
    label: str
    field_type: UIFieldType
    validation: UIFieldValidation = Field(default_factory=UIFieldValidation)
    placeholder: str | None = None
    options: list[str] = Field(default_factory=list)
    depends_on: str | None = None       # conditional visibility


class UIComponentLayout(BaseSchema):
    grid_span_cols: int = Field(default=12, description="Width on a 12-col grid")
    row_order: int = Field(default=0, description="Vertical order index on the page")


class UIComponent(BaseSchema):
    component_id: str
    component_type: Literal["form", "table", "card", "chart", "stat_banner", "navbar", "modal"]
    title: str
    layout_config: UIComponentLayout = Field(default_factory=UIComponentLayout)

    # Data bindings
    data_source: str | None = None  # GET endpoint feeding this component
    submit_endpoint: str | None = None  # mutation endpoint for forms
    submit_method: HTTPMethod | None = None  # POST, PUT, PATCH

    # Visual
    fields: list[UIField] = Field(default_factory=list)
    columns: list[str] = Field(default_factory=list)
    actions: list[str] = Field(default_factory=list)


class UIPage(BaseSchema):
    page_id: str
    route: str = Field(..., description="Frontend route e.g. /dashboard/contacts")
    title: str
    page_type: PageType
    layout: Literal["full", "sidebar", "centered", "split"] = "sidebar"
    components: list[UIComponent] = Field(default_factory=list)
    auth_required: bool = True
    allowed_roles: list[str] = Field(default_factory=list)


class NavItem(BaseSchema):
    label: str
    route: str
    icon: str | None = None
    role_guard: list[str] = Field(default_factory=list)


class Theme(BaseSchema):
    primary: str = "#4F46E5"
    secondary: str = "#10B981"
    mode: Literal["light", "dark"] = "light"


class UISchema(BaseSchema):
    pages: list[UIPage]
    nav_items: list[NavItem] = Field(default_factory=list)
    theme: Theme = Field(default_factory=Theme)