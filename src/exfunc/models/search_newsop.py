"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .googlenews import GoogleNews, GoogleNewsTypedDict
from enum import Enum
from exfunc.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class TimePublished(str, Enum):
    r"""Filter news articles published after this date"""

    ANYTIME = "anytime"
    ONEH = "1h"
    ONED = "1d"
    SEVEND = "7d"
    ONEY = "1y"


class SearchNewsRequestBodyTypedDict(TypedDict):
    query: str
    r"""The search query for news articles"""
    country_code: NotRequired[str]
    r"""The country code for filtering news"""
    per_page: NotRequired[int]
    r"""Number of news articles to return per page (default is 10)"""
    time_published: NotRequired[TimePublished]
    r"""Filter news articles published after this date"""


class SearchNewsRequestBody(BaseModel):
    query: str
    r"""The search query for news articles"""

    country_code: Optional[str] = None
    r"""The country code for filtering news"""

    per_page: Optional[int] = None
    r"""Number of news articles to return per page (default is 10)"""

    time_published: Optional[TimePublished] = None
    r"""Filter news articles published after this date"""


class SearchNewsResponseBodyTypedDict(TypedDict):
    r"""SearchNews API successful response"""

    news: NotRequired[List[GoogleNewsTypedDict]]


class SearchNewsResponseBody(BaseModel):
    r"""SearchNews API successful response"""

    news: Optional[List[GoogleNews]] = None
