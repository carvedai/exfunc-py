"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .googlejobposting import GoogleJobPosting, GoogleJobPostingTypedDict
from exfunc.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class GoogleGetJobPostingRequestBodyTypedDict(TypedDict):
    job_posting_id: str
    r"""The ID of the job posting to retrieve"""


class GoogleGetJobPostingRequestBody(BaseModel):
    job_posting_id: str
    r"""The ID of the job posting to retrieve"""


class GoogleGetJobPostingResponseBodyTypedDict(TypedDict):
    r"""GetJobPosting API successful response"""

    job_posting: NotRequired[GoogleJobPostingTypedDict]


class GoogleGetJobPostingResponseBody(BaseModel):
    r"""GetJobPosting API successful response"""

    job_posting: Optional[GoogleJobPosting] = None
