"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from enum import Enum
from exfunc.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class DatePosted(str, Enum):
    r"""Filter for job postings based on when they were posted"""

    PAST_24_HOURS = "Past 24 hours"
    PAST_WEEK = "Past Week"
    PAST_MONTH = "Past Month"


class Salary(str, Enum):
    r"""Salary range to filter job postings"""

    DOLLAR_40_000_PLUS_ = "$40,000+"
    DOLLAR_60_000_PLUS_ = "$60,000+"
    DOLLAR_80_000_PLUS_ = "$80,000+"
    DOLLAR_100_000_PLUS_ = "$100,000+"
    DOLLAR_120_000_PLUS_ = "$120,000+"


class JobTypes(str, Enum):
    r"""Job types to filter (e.g., Full-time, Part-time)"""

    CONTRACT = "Contract"
    FULL_TIME = "Full-time"
    PART_TIME = "Part-time"
    TEMPORARY = "Temporary"
    VOLUNTEER = "Volunteer"


class WorkTypes(str, Enum):
    r"""Work types to filter (e.g., Remote, On-site)"""

    ON_SITE = "On-site"
    REMOTE = "Remote"
    HYBRID = "Hybrid"


class SearchJobPostingsRequestBodyTypedDict(TypedDict):
    keywords: str
    r"""Keywords to search for in job postings"""
    location: str
    r"""Location to filter job postings"""
    date_posted: NotRequired[DatePosted]
    r"""Filter for job postings based on when they were posted"""
    salary: NotRequired[Salary]
    r"""Salary range to filter job postings"""
    job_types: NotRequired[List[JobTypes]]
    work_types: NotRequired[List[WorkTypes]]
    company_uids: NotRequired[List[str]]
    page: NotRequired[int]
    r"""Page number for pagination (default is 1)"""


class SearchJobPostingsRequestBody(BaseModel):
    keywords: str
    r"""Keywords to search for in job postings"""

    location: str
    r"""Location to filter job postings"""

    date_posted: Optional[DatePosted] = None
    r"""Filter for job postings based on when they were posted"""

    salary: Optional[Salary] = None
    r"""Salary range to filter job postings"""

    job_types: Optional[List[JobTypes]] = None

    work_types: Optional[List[WorkTypes]] = None

    company_uids: Optional[List[str]] = None

    page: Optional[int] = None
    r"""Page number for pagination (default is 1)"""


class JobPostingsTypedDict(TypedDict):
    url: NotRequired[str]
    r"""URL to the job posting"""
    title: NotRequired[str]
    r"""Title of the job"""
    location: NotRequired[str]
    r"""Job location"""
    date_posted: NotRequired[datetime]
    r"""Date when the job was posted"""
    company_name: NotRequired[str]
    r"""Name of the company offering the job"""
    company_url: NotRequired[str]
    r"""URL to the company's profile"""


class JobPostings(BaseModel):
    url: Optional[str] = None
    r"""URL to the job posting"""

    title: Optional[str] = None
    r"""Title of the job"""

    location: Optional[str] = None
    r"""Job location"""

    date_posted: Optional[datetime] = None
    r"""Date when the job was posted"""

    company_name: Optional[str] = None
    r"""Name of the company offering the job"""

    company_url: Optional[str] = None
    r"""URL to the company's profile"""


class SearchJobPostingsResponseBodyTypedDict(TypedDict):
    r"""SearchJobPostings API successful response"""

    job_postings: NotRequired[List[JobPostingsTypedDict]]


class SearchJobPostingsResponseBody(BaseModel):
    r"""SearchJobPostings API successful response"""

    job_postings: Optional[List[JobPostings]] = None
