# Skyscanner
(*skyscanner*)

## Overview

### Available Operations

* [search_one_way](#search_one_way) - Search one-way flights on SkyScanner
* [search_roundtrip](#search_roundtrip) - Search roundtrip flights on SkyScanner

## search_one_way

Search one-way flights on SkyScanner for given origin, destination, and departure date

### Example Usage

```python
from exfunc import Exfunc
import os

s = Exfunc(
    api_key=os.getenv("EXFUNC_API_KEY", ""),
)

res = s.skyscanner.search_one_way(request={
    "origin": "<value>",
    "destination": "<value>",
    "depart_date": "<value>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `request`                                                                 | [models.SearchOneWayRequestBody](../../models/searchonewayrequestbody.md) | :heavy_check_mark:                                                        | The request object to use for the request.                                |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.SearchOneWayResponseBody](../../models/searchonewayresponsebody.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.UserError   | 400                | application/json   |
| models.ServerError | 500                | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## search_roundtrip

Search roundtrip flights on SkyScanner for given origin, destination, departure date and return date

### Example Usage

```python
from exfunc import Exfunc
import os

s = Exfunc(
    api_key=os.getenv("EXFUNC_API_KEY", ""),
)

res = s.skyscanner.search_roundtrip(request={
    "origin": "<value>",
    "destination": "<value>",
    "depart_date": "<value>",
    "return_date": "<value>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `request`                                                                       | [models.SearchRoundtripRequestBody](../../models/searchroundtriprequestbody.md) | :heavy_check_mark:                                                              | The request object to use for the request.                                      |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Response

**[models.SearchRoundtripResponseBody](../../models/searchroundtripresponsebody.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.UserError   | 400                | application/json   |
| models.ServerError | 500                | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |