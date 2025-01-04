# Skyscanner
(*skyscanner*)

## Overview

### Available Operations

* [search_flights](#search_flights) - Search flights on SkyScanner

## search_flights

Search flights on SkyScanner for given origin, destination, departure date and return date

### Example Usage

```python
import exfunc
from exfunc import Exfunc
import os

with Exfunc(
    api_key=os.getenv("EXFUNC_API_KEY", ""),
) as exfunc:

    res = exfunc.skyscanner.search_flights(request={
        "origin": "<value>",
        "destination": "<value>",
        "flight_type": exfunc.FlightType.ROUNDTRIP,
        "depart_date": "<value>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `request`                                                                   | [models.SearchFlightsRequestBody](../../models/searchflightsrequestbody.md) | :heavy_check_mark:                                                          | The request object to use for the request.                                  |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[models.SearchFlightsResponseBody](../../models/searchflightsresponsebody.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.UserError   | 400                | application/json   |
| models.ServerError | 500                | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |