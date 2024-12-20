"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .tweet import Tweet, TweetTypedDict
from exfunc.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class GetTweetRequestBodyTypedDict(TypedDict):
    tweet_id: str
    r"""The ID of the tweet to retrieve"""


class GetTweetRequestBody(BaseModel):
    tweet_id: str
    r"""The ID of the tweet to retrieve"""


class GetTweetResponseBodyTypedDict(TypedDict):
    r"""GetTweet API successful response"""

    tweet: NotRequired[TweetTypedDict]


class GetTweetResponseBody(BaseModel):
    r"""GetTweet API successful response"""

    tweet: Optional[Tweet] = None
