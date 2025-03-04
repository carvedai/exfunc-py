"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .googleproduct import GoogleProduct, GoogleProductTypedDict
from enum import Enum
from exfunc.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class SortBy(str, Enum):
    r"""Sort the results by a specific field"""

    BEST_MATCH = "best_match"
    TOP_RATED = "top_rated"
    LOWEST_PRICE = "lowest_price"
    HIGHEST_PRICE = "highest_price"


class ProductCondition(str, Enum):
    r"""Filter products by condition"""

    ANY = "any"
    NEW = "new"
    USED = "used"
    REFURBISHED = "refurbished"


class SearchProductsRequestBodyTypedDict(TypedDict):
    query: str
    r"""The search query for products"""
    country_code: NotRequired[str]
    r"""The country code for filtering products"""
    page: NotRequired[int]
    r"""Page number for pagination (default is 1)"""
    per_page: NotRequired[int]
    r"""Number of products to return per page (default is 10)"""
    sort_by: NotRequired[SortBy]
    r"""Sort the results by a specific field"""
    product_condition: NotRequired[ProductCondition]
    r"""Filter products by condition"""


class SearchProductsRequestBody(BaseModel):
    query: str
    r"""The search query for products"""

    country_code: Optional[str] = None
    r"""The country code for filtering products"""

    page: Optional[int] = None
    r"""Page number for pagination (default is 1)"""

    per_page: Optional[int] = None
    r"""Number of products to return per page (default is 10)"""

    sort_by: Optional[SortBy] = None
    r"""Sort the results by a specific field"""

    product_condition: Optional[ProductCondition] = None
    r"""Filter products by condition"""


class SearchProductsResponseBodyTypedDict(TypedDict):
    r"""SearchProducts API successful response"""

    products: NotRequired[List[GoogleProductTypedDict]]


class SearchProductsResponseBody(BaseModel):
    r"""SearchProducts API successful response"""

    products: Optional[List[GoogleProduct]] = None
