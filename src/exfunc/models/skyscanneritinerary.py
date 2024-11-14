"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .skyscannerleg import SkyScannerLeg, SkyScannerLegTypedDict
from exfunc.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class SkyScannerItineraryTypedDict(TypedDict):
    price: NotRequired[str]
    r"""The price for the itinerary"""
    legs: NotRequired[List[SkyScannerLegTypedDict]]


class SkyScannerItinerary(BaseModel):
    price: Optional[str] = None
    r"""The price for the itinerary"""

    legs: Optional[List[SkyScannerLeg]] = None
