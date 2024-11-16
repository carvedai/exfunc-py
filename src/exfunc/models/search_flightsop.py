"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .skyscanneritinerary import SkyScannerItinerary, SkyScannerItineraryTypedDict
from enum import Enum
from exfunc.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class FlightType(str, Enum):
    r"""The type of the flight"""

    ONE_WAY = "one-way"
    ROUNDTRIP = "roundtrip"


class Stops(str, Enum):
    DIRECT = "Direct"
    ONE_STOP = "1 Stop"
    TWO_PLUS_STOPS = "2+ Stops"


class CabinClass(str, Enum):
    r"""The cabin class filter"""

    ECONOMY = "economy"
    PREMIUM_ECONOMY = "premium_economy"
    BUSINESS = "business"
    FIRST = "first"


class SearchFlightsRequestBodyTypedDict(TypedDict):
    origin: str
    r"""The origin location of the itinerary"""
    destination: str
    r"""The destination location of the itinerary"""
    flight_type: FlightType
    r"""The type of the flight"""
    depart_date: str
    r"""The departure date of the itinerary. The format has to be YYYY-MM-DD"""
    return_date: NotRequired[str]
    r"""The return date of the itinerary. The format has to be YYYY-MM-DD. If the flight type is roundtrip, this field is required."""
    stops: NotRequired[List[Stops]]
    r"""The list of filter values for number of stops"""
    num_adults: NotRequired[float]
    r"""The number of adults for the itinerary"""
    num_children: NotRequired[float]
    r"""The number of children for the itinerary"""
    num_infants: NotRequired[float]
    r"""The number of infants for the itinerary"""
    cabin_class: NotRequired[CabinClass]
    r"""The cabin class filter"""
    include_origin_nearby_airports: NotRequired[bool]
    r"""Boolean to indicate whether to include nearby origin airports in the results or not"""
    include_destination_nearby_airports: NotRequired[bool]
    r"""Boolean to indicate whether to include nearby destination airports in the results or not"""


class SearchFlightsRequestBody(BaseModel):
    origin: str
    r"""The origin location of the itinerary"""

    destination: str
    r"""The destination location of the itinerary"""

    flight_type: FlightType
    r"""The type of the flight"""

    depart_date: str
    r"""The departure date of the itinerary. The format has to be YYYY-MM-DD"""

    return_date: Optional[str] = None
    r"""The return date of the itinerary. The format has to be YYYY-MM-DD. If the flight type is roundtrip, this field is required."""

    stops: Optional[List[Stops]] = None
    r"""The list of filter values for number of stops"""

    num_adults: Optional[float] = 1
    r"""The number of adults for the itinerary"""

    num_children: Optional[float] = 0
    r"""The number of children for the itinerary"""

    num_infants: Optional[float] = 0
    r"""The number of infants for the itinerary"""

    cabin_class: Optional[CabinClass] = None
    r"""The cabin class filter"""

    include_origin_nearby_airports: Optional[bool] = False
    r"""Boolean to indicate whether to include nearby origin airports in the results or not"""

    include_destination_nearby_airports: Optional[bool] = False
    r"""Boolean to indicate whether to include nearby destination airports in the results or not"""


class SearchFlightsResponseBodyTypedDict(TypedDict):
    r"""SearchFlights API successful response"""

    itineraries: NotRequired[List[SkyScannerItineraryTypedDict]]


class SearchFlightsResponseBody(BaseModel):
    r"""SearchFlights API successful response"""

    itineraries: Optional[List[SkyScannerItinerary]] = None