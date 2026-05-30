"""
Shared enums and primitive types used across multiple schemas.
Nothing here imports from other schema files.
"""
from __future__ import annotations
from enum import Enum


class AppCategory(str, Enum):
    CRM = "crm"
    ECOMMERCE = "ecommerce"
    SAAS_DASHBOARD = "saas_dashboard"
    INTERNAL_TOOL = "internal_tool"
    MARKETPLACE = "marketplace"
    SOCIAL = "social"
    CUSTOM = "custom"


class ScaleHint(str, Enum):
    MVP = "mvp"
    PRODUCTION = "production"
    ENTERPRISE = "enterprise"


class AuthStrategy(str, Enum):
    JWT = "jwt"
    SESSION = "session"
    OAUTH2 = "oauth2"
    NONE = "none"


class HTTPMethod(str, Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    PATCH = "PATCH"
    DELETE = "DELETE"


class FieldType(str, Enum):
    STRING = "string"
    INT = "int"
    FLOAT = "float"
    BOOL = "bool"
    DATETIME = "datetime"
    DATE = "date"
    UUID = "uuid"
    EMAIL = "email"
    ENUM = "enum"
    JSON = "json"
    FOREIGN_KEY = "foreign_key"


class PageType(str, Enum):
    LIST = "list"
    DETAIL = "detail"
    FORM = "form"
    DASHBOARD = "dashboard"
    AUTH = "auth"
    SETTINGS = "settings"
    CUSTOM = "custom"


class Severity(str, Enum):
    CRITICAL = "critical"
    WARNING = "warning"
    INFO = "info"


class Priority(str, Enum):
    CORE = "core"
    SECONDARY = "secondary"
    OPTIONAL = "optional"


class Actor(str, Enum):
    USER = "user"
    SYSTEM = "system"
    EXTERNAL = "external"


class UIFieldType(str, Enum):
    TEXT = "text"
    EMAIL = "email"
    PASSWORD = "password"
    NUMBER = "number"
    SELECT = "select"
    MULTI_SELECT = "multi_select"
    CHECKBOX = "checkbox"
    DATE = "date"
    DATETIME = "datetime"
    TEXTAREA = "textarea"
    FILE = "file"
    HIDDEN = "hidden"

class APIParamType(str, Enum):
    STRING = "string"
    INT = "int"
    FLOAT = "float"
    BOOL = "bool"
    DATETIME = "datetime"
    DATE = "date"
    UUID = "uuid"
    EMAIL = "email"

