"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .linkedinjobposting import LinkedInJobPosting, LinkedInJobPostingTypedDict
from exfunc.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class GetJobPostingRequestBodyTypedDict(TypedDict):
    job_posting_url: str
    r"""The LinkedIn URL of the job posting to enrich"""


class GetJobPostingRequestBody(BaseModel):
    job_posting_url: str
    r"""The LinkedIn URL of the job posting to enrich"""


class GetJobPostingResponseBodyTypedDict(TypedDict):
    r"""GetJobPosting API successful response"""

    job_posting: NotRequired[LinkedInJobPostingTypedDict]


class GetJobPostingResponseBody(BaseModel):
    r"""GetJobPosting API successful response"""

    job_posting: Optional[LinkedInJobPosting] = None
