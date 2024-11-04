"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .yelpreview import YelpReview, YelpReviewTypedDict
from enum import Enum
from exfunc.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class GetBusinessReviewsSortBy(str, Enum):
    r"""The criteria to sort reviews (e.g., \"best_match\", \"newest\", etc.)"""

    BEST_MATCH = "best_match"
    NEWEST = "newest"
    OLDEST = "oldest"
    HIGHEST_RATED = "highest_rated"
    LOWEST_RATED = "lowest_rated"
    ELITES = "elites"


class GetBusinessReviewsRequestBodyTypedDict(TypedDict):
    business_id: str
    r"""The ID of the business to retrieve reviews for"""
    sort_by: NotRequired[GetBusinessReviewsSortBy]
    r"""The criteria to sort reviews (e.g., \"best_match\", \"newest\", etc.)"""
    page: NotRequired[int]
    r"""The page number of results to retrieve (default is 1)"""
    per_page: NotRequired[int]
    r"""The number of reviews to retrieve per page (default is 10)"""


class GetBusinessReviewsRequestBody(BaseModel):
    business_id: str
    r"""The ID of the business to retrieve reviews for"""

    sort_by: Optional[GetBusinessReviewsSortBy] = None
    r"""The criteria to sort reviews (e.g., \"best_match\", \"newest\", etc.)"""

    page: Optional[int] = None
    r"""The page number of results to retrieve (default is 1)"""

    per_page: Optional[int] = None
    r"""The number of reviews to retrieve per page (default is 10)"""


class GetBusinessReviewsResponseBodyTypedDict(TypedDict):
    r"""GetBusinessReviews API successful response"""

    reviews: NotRequired[List[YelpReviewTypedDict]]


class GetBusinessReviewsResponseBody(BaseModel):
    r"""GetBusinessReviews API successful response"""

    reviews: Optional[List[YelpReview]] = None
