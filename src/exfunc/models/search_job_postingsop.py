"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from exfunc.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class SearchJobPostingsDatePosted(str, Enum):
    r"""Filter for job postings based on when they were posted"""

    ANY_TIME = "Any time"
    PAST_24_HOURS = "Past 24 hours"
    PAST_WEEK = "Past Week"
    PAST_MONTH = "Past Month"


class SearchJobPostingsSalary(str, Enum):
    r"""Salary range to filter job postings"""

    DOLLAR_40_000_PLUS_ = "$40,000+"
    DOLLAR_60_000_PLUS_ = "$60,000+"
    DOLLAR_80_000_PLUS_ = "$80,000+"
    DOLLAR_100_000_PLUS_ = "$100,000+"
    DOLLAR_120_000_PLUS_ = "$120,000+"
    DOLLAR_140_000_PLUS_ = "$140,000+"
    DOLLAR_160_000_PLUS_ = "$160,000+"
    DOLLAR_180_000_PLUS_ = "$180,000+"
    DOLLAR_200_000_PLUS_ = "$200,000+"


class JobType(str, Enum):
    r"""Job type to filter (e.g., Full-time, Part-time)"""

    CONTRACT = "Contract"
    FULL_TIME = "Full-time"
    PART_TIME = "Part-time"
    INTERNSHIP = "Internship"


class WorkType(str, Enum):
    r"""Work type to filter (e.g., Remote, On-site)"""

    ON_SITE = "On-site"
    REMOTE = "Remote"
    HYBRID = "Hybrid"


class ExperienceLevel(str, Enum):
    r"""Experience level to filter (e.g., Associate, Executive)"""

    ASSOCIATE = "Associate"
    DIRECTOR = "Director"
    ENTRY_LEVEL = "Entry Level"
    EXECUTIVE = "Executive"
    INTERNSHIP = "Internship"
    MID_SENIOR_LEVEL = "Mid-Senior Level"


class SearchJobPostingsSortBy(str, Enum):
    r"""The criteria to sort results"""

    MOST_RECENT = "Most Recent"
    MOST_RELEVANT = "Most Relevant"


class SearchJobPostingsRequestBodyTypedDict(TypedDict):
    keywords: NotRequired[str]
    r"""Keywords to search for in job postings"""
    location: NotRequired[str]
    r"""Location to filter job postings"""
    date_posted: NotRequired[SearchJobPostingsDatePosted]
    r"""Filter for job postings based on when they were posted"""
    salary: NotRequired[SearchJobPostingsSalary]
    r"""Salary range to filter job postings"""
    job_type: NotRequired[JobType]
    r"""Job type to filter (e.g., Full-time, Part-time)"""
    work_type: NotRequired[WorkType]
    r"""Work type to filter (e.g., Remote, On-site)"""
    experience_level: NotRequired[ExperienceLevel]
    r"""Experience level to filter (e.g., Associate, Executive)"""
    company_uids: NotRequired[List[str]]
    r"""List of company unique identifiers to filter"""
    sort_by: NotRequired[SearchJobPostingsSortBy]
    r"""The criteria to sort results"""
    page: NotRequired[int]
    r"""Page number for pagination (default is 1)"""


class SearchJobPostingsRequestBody(BaseModel):
    keywords: Optional[str] = None
    r"""Keywords to search for in job postings"""

    location: Optional[str] = None
    r"""Location to filter job postings"""

    date_posted: Optional[SearchJobPostingsDatePosted] = None
    r"""Filter for job postings based on when they were posted"""

    salary: Optional[SearchJobPostingsSalary] = None
    r"""Salary range to filter job postings"""

    job_type: Optional[JobType] = None
    r"""Job type to filter (e.g., Full-time, Part-time)"""

    work_type: Optional[WorkType] = None
    r"""Work type to filter (e.g., Remote, On-site)"""

    experience_level: Optional[ExperienceLevel] = None
    r"""Experience level to filter (e.g., Associate, Executive)"""

    company_uids: Optional[List[str]] = None
    r"""List of company unique identifiers to filter"""

    sort_by: Optional[SearchJobPostingsSortBy] = None
    r"""The criteria to sort results"""

    page: Optional[int] = None
    r"""Page number for pagination (default is 1)"""


class JobPostingsTypedDict(TypedDict):
    url: NotRequired[str]
    r"""URL to the job posting"""
    title: NotRequired[str]
    r"""Title of the job"""
    location: NotRequired[str]
    r"""Job location"""
    date_posted: NotRequired[str]
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

    date_posted: Optional[str] = None
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
