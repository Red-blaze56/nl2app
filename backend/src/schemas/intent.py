"""
Stage 1 — Intent Extraction Schema

This module defines the structured intermediate representation (IR)
generated from the user's natural language application request.

Purpose:
    Convert ambiguous natural language into deterministic,
    machine-processable compiler contracts.

Pipeline Position:
    Raw Prompt -->  IntentModel --> DesignModel --> AppConfig

Responsibilities:
    - Capture high-level application goals
    - Extract requested features and dependencies
    - Detect authentication/payment requirements
    - Infer domain entities
    - Represent ambiguity explicitly
    - Provide structured input for system design generation
"""
from pydantic import Field
from typing import Literal

from .base import BaseSchema
from .common import AppCategory, AuthStrategy, Priority, ScaleHint

class Features(BaseSchema):
    name:str = Field(..., description="Name of the feature")
    description:str = Field(..., description="Description of the feature")
    priority: Priority 
    requires: list[str]

class AuthRequirement(BaseSchema):
    required: bool
    strategy: AuthStrategy = AuthStrategy.JWT
    roles: list[str] = Field(default_factory=list, description="List of roles required for authentication")

class PaymentRequirement(BaseSchema):
    required: bool
    provider : list[Literal["stripe","razorpay","paypal","Gpay","paytm"]] = Field(default_factory=list, description="List of payment providers")


class Intent(BaseSchema):
    app_name: str = Field(..., description="Name of the app")
    app_category: AppCategory
    description: str = Field(..., description="Description of the intent")
    features: list[Features] = Field(default=[], description="List of features associated with the intent")
    entities: list[str] = Field(default=[], description="List of entities associated with the intent")
    auth: AuthRequirement
    payment: PaymentRequirement
    scale_hint: ScaleHint = ScaleHint.PRODUCTION
    ambiguities: list[str] = Field(default_factory=list, description="List of ambiguities in the intent")
    confidence_score: float = Field(ge=0.0, le=1.0, description="Confidence score of the intent prediction")