"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .zillowproperty import ZillowProperty, ZillowPropertyTypedDict
from exfunc.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class GetPropertyRequestBodyTypedDict(TypedDict):
    property_id: str
    r"""The ID of the property"""


class GetPropertyRequestBody(BaseModel):
    property_id: str
    r"""The ID of the property"""


class GetPropertyResponseBodyTypedDict(TypedDict):
    r"""GetProperty API successful response"""

    property: NotRequired[ZillowPropertyTypedDict]


class GetPropertyResponseBody(BaseModel):
    r"""GetProperty API successful response"""

    property: Optional[ZillowProperty] = None
