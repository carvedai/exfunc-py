"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from exfunc.types import BaseModel
from typing import Dict, List, Optional
from typing_extensions import NotRequired, TypedDict


class GoogleProductTypedDict(TypedDict):
    product_id: NotRequired[str]
    r"""The unique identifier for the product"""
    title: NotRequired[str]
    r"""The title of the product"""
    description: NotRequired[str]
    r"""A detailed description of the product"""
    photos: NotRequired[List[str]]
    r"""An array of URLs for the product photos"""
    attributes: NotRequired[Dict[str, str]]
    r"""A set of attributes for the product, represented as key-value pairs"""
    rating: NotRequired[float]
    r"""The average rating of the product"""
    page_url: NotRequired[str]
    r"""The URL link to the product page"""
    num_reviews: NotRequired[int]
    r"""The total number of reviews for the product"""
    reviews_per_rating: NotRequired[Dict[str, int]]
    r"""The number of reviews for each rating level"""
    product_details: NotRequired[Dict[str, str]]
    r"""Detailed information about the product"""
    product_specs: NotRequired[Dict[str, str]]
    r"""Technical specifications of the product"""


class GoogleProduct(BaseModel):
    product_id: Optional[str] = None
    r"""The unique identifier for the product"""

    title: Optional[str] = None
    r"""The title of the product"""

    description: Optional[str] = None
    r"""A detailed description of the product"""

    photos: Optional[List[str]] = None
    r"""An array of URLs for the product photos"""

    attributes: Optional[Dict[str, str]] = None
    r"""A set of attributes for the product, represented as key-value pairs"""

    rating: Optional[float] = None
    r"""The average rating of the product"""

    page_url: Optional[str] = None
    r"""The URL link to the product page"""

    num_reviews: Optional[int] = None
    r"""The total number of reviews for the product"""

    reviews_per_rating: Optional[Dict[str, int]] = None
    r"""The number of reviews for each rating level"""

    product_details: Optional[Dict[str, str]] = None
    r"""Detailed information about the product"""

    product_specs: Optional[Dict[str, str]] = None
    r"""Technical specifications of the product"""
