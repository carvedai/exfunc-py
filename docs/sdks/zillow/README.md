# Zillow
(*zillow*)

## Overview

### Available Operations

* [get_property](#get_property) - Get property details from Zillow
* [search_properties](#search_properties) - Search for properties on Zillow

## get_property

Get property details on Zillow for a given property ID

### Example Usage

```python
from exfunc import Exfunc
import os

s = Exfunc(
    api_key=os.getenv("EXFUNC_API_KEY", ""),
)

res = s.zillow.get_property(request={
    "property_id": "<id>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `request`                                                               | [models.GetPropertyRequestBody](../../models/getpropertyrequestbody.md) | :heavy_check_mark:                                                      | The request object to use for the request.                              |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[models.GetPropertyResponseBody](../../models/getpropertyresponsebody.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.UserError   | 400                | application/json   |
| models.ServerError | 500                | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## search_properties

Search for properties on Zillow for a given location, listing status, and other criteria

### Example Usage

```python
import exfunc
from exfunc import Exfunc
import os

s = Exfunc(
    api_key=os.getenv("EXFUNC_API_KEY", ""),
)

res = s.zillow.search_properties(request={
    "location": "<value>",
    "listing_status": exfunc.ListingStatus.FOR_RENT,
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `request`                                                                         | [models.SearchPropertiesRequestBody](../../models/searchpropertiesrequestbody.md) | :heavy_check_mark:                                                                | The request object to use for the request.                                        |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.SearchPropertiesResponseBody](../../models/searchpropertiesresponsebody.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.UserError   | 400                | application/json   |
| models.ServerError | 500                | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |