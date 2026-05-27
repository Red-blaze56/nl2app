"""
Stage 2 - System Architecture Design Schema

This module designs the blueprint for the system architecture based on the extracted intent.

Purpose:
    Translate the intent into a structured design that guides the implementation phase.

Pipeline Position:
    Raw Prompt -->  IntentModel --> DesignModel --> AppConfig

Responsibilities:
    - Define application modules
    - Define pages and navigation
    - Define workflows and user journeys
    - Define entity relationships
    - Create architectural blueprints
    - Provide structured input for schema generation
"""

from __future__ import annotations
from typing import Literal, Any
from pydantic import Field

from .base import BaseSchema
from .common import FieldType, PageType, Actor, HTTPMethod

class EntityField(BaseSchema):
    name: str
    field_type: FieldType
    required: bool = True
    unique: bool = False
    indexed: bool = False
    default: Any = None
    enum_values: list[str] = Field(default_factory=list)
    references: str | None = None       # entity name if FK


class Entity(BaseSchema):
    name: str                           # PascalCase: Contact
    table_name: str                     # snake_case: contacts
    fields: list[EntityField]
    owns: list[str] = Field(default_factory=list)
    soft_delete: bool = False
    timestamps: bool = True             # adds created_at, updated_at


class Permission(BaseSchema):
    resource: str
    actions: list[Literal["create", "read", "update", "delete", "list"]]


class Role(BaseSchema):
    name: str
    inherits: str | None = None
    permissions: list[Permission] = Field(default_factory=list)
    is_default: bool = False


class PageBlueprint(BaseSchema):
    name: str
    route: str
    page_type: PageType
    primary_entity: str | None = None
    required_roles: list[str] = Field(default_factory=list)
    actions: list[str] = Field(default_factory=list)
    linked_pages: list[str] = Field(default_factory=list)


class FlowStep(BaseSchema):
    step: int
    description: str
    actor: Actor
    involves_entity: str | None = None


class AppFlow(BaseSchema):
    name: str
    trigger_method: HTTPMethod
    trigger_path: str    # e.g. "POST /auth/register"
    steps: list[FlowStep] = Field(default_factory=list)
    produces: list[str] = Field(default_factory=list)


class TechStack(BaseSchema): 
    frontend: Literal["react", "nextjs", "vue", "html"] = "react" 
    backend: Literal["fastapi", "nodejs", "express"] = "fastapi" 
    database: Literal["postgresql", "sqlite", "mongodb"] = "postgresql"


class SystemDesignOutput(BaseSchema):
    entities: list[Entity]
    roles: list[Role]
    pages: list[PageBlueprint]
    flows: list[AppFlow]
    tech_stack: TechStack = Field(default_factory=TechStack)
    design_notes: list[str] = Field(default_factory=list)