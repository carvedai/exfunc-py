"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .glassdoorjobposting import GlassdoorJobPosting, GlassdoorJobPostingTypedDict
from enum import Enum
from exfunc.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class DatePosted(str, Enum):
    r"""Filter for job postings based on when they were posted"""

    ANY_TIME = "Any time"
    PAST_24_HOURS = "Past 24 hours"
    PAST_3_DAYS = "Past 3 days"
    PAST_WEEK = "Past Week"
    PAST_MONTH = "Past Month"


class GlassdoorSearchJobPostingsRequestBodyTypedDict(TypedDict):
    query: NotRequired[str]
    r"""The search query for job postings"""
    location: NotRequired[str]
    r"""Location to filter job postings"""
    date_posted: NotRequired[DatePosted]
    r"""Filter for job postings based on when they were posted"""
    next_token: NotRequired[Nullable[str]]
    r"""Next token for pagination"""


class GlassdoorSearchJobPostingsRequestBody(BaseModel):
    query: Optional[str] = None
    r"""The search query for job postings"""

    location: Optional[str] = None
    r"""Location to filter job postings"""

    date_posted: Optional[DatePosted] = None
    r"""Filter for job postings based on when they were posted"""

    next_token: OptionalNullable[str] = UNSET
    r"""Next token for pagination"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["query", "location", "date_posted", "next_token"]
        nullable_fields = ["next_token"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m


class GlassdoorSearchJobPostingsResponseBodyTypedDict(TypedDict):
    r"""SearchJobPostings API successful response"""

    job_postings: NotRequired[List[GlassdoorJobPostingTypedDict]]
    next_token: NotRequired[str]
    r"""Next token for pagination"""


class GlassdoorSearchJobPostingsResponseBody(BaseModel):
    r"""SearchJobPostings API successful response"""

    job_postings: Optional[List[GlassdoorJobPosting]] = None

    next_token: Optional[str] = None
    r"""Next token for pagination"""
