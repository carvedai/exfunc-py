"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .googleproduct import GoogleProduct, GoogleProductTypedDict
from exfunc.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class GetProductRequestBodyTypedDict(TypedDict):
    product_id: str
    r"""The ID of the product to retrieve"""
    country_code: NotRequired[str]
    r"""The country code for the product"""


class GetProductRequestBody(BaseModel):
    product_id: str
    r"""The ID of the product to retrieve"""

    country_code: Optional[str] = None
    r"""The country code for the product"""


class GetProductResponseBodyTypedDict(TypedDict):
    r"""GetProduct API successful response"""

    product: NotRequired[GoogleProductTypedDict]


class GetProductResponseBody(BaseModel):
    r"""GetProduct API successful response"""

    product: Optional[GoogleProduct] = None
