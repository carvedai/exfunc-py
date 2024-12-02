"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .googlejobposting import GoogleJobPosting, GoogleJobPostingTypedDict
from enum import Enum
from exfunc.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class DatePosted(str, Enum):
    r"""Filter for job postings based on when they were posted"""

    ANY_TIME = "Any time"
    PAST_24_HOURS = "Past 24 hours"
    PAST_3_DAYS = "Past 3 days"
    PAST_WEEK = "Past Week"
    PAST_MONTH = "Past Month"


class JobTypes(str, Enum):
    CONTRACT = "Contract"
    FULL_TIME = "Full-time"
    PART_TIME = "Part-time"
    INTERNSHIP = "Internship"


class GoogleSearchJobPostingsRequestBodyTypedDict(TypedDict):
    query: str
    r"""The search query for job postings"""
    location: NotRequired[str]
    r"""Location to filter job postings"""
    country_code: NotRequired[str]
    r"""The country code to filter job postings"""
    date_posted: NotRequired[DatePosted]
    r"""Filter for job postings based on when they were posted"""
    job_types: NotRequired[List[JobTypes]]
    r"""Job types to filter (e.g., Full-time, Part-time)"""
    page: NotRequired[int]
    r"""Page number for pagination (default is 1)"""
    per_page: NotRequired[int]
    r"""Number of news articles to return per page (default is 10)"""


class GoogleSearchJobPostingsRequestBody(BaseModel):
    query: str
    r"""The search query for job postings"""

    location: Optional[str] = None
    r"""Location to filter job postings"""

    country_code: Optional[str] = "us"
    r"""The country code to filter job postings"""

    date_posted: Optional[DatePosted] = None
    r"""Filter for job postings based on when they were posted"""

    job_types: Optional[List[JobTypes]] = None
    r"""Job types to filter (e.g., Full-time, Part-time)"""

    page: Optional[int] = None
    r"""Page number for pagination (default is 1)"""

    per_page: Optional[int] = None
    r"""Number of news articles to return per page (default is 10)"""


class GoogleSearchJobPostingsResponseBodyTypedDict(TypedDict):
    r"""SearchJobPostings API successful response"""

    job_postings: NotRequired[List[GoogleJobPostingTypedDict]]


class GoogleSearchJobPostingsResponseBody(BaseModel):
    r"""SearchJobPostings API successful response"""

    job_postings: Optional[List[GoogleJobPosting]] = None
