# Yelp
(*yelp*)

## Overview

### Available Operations

* [get_business](#get_business) - Get business details from Yelp
* [get_business_reviews](#get_business_reviews) - Get Yelp reviews for a business
* [search_businesses](#search_businesses) - Search for businesses on Yelp

## get_business

Get business details from Yelp for a given business ID

### Example Usage

<!-- UsageSnippet language="python" operationID="get-business" method="post" path="/yelp/get-business" -->
```python
from exfunc import Exfunc
import os


with Exfunc(
    api_key=os.getenv("EXFUNC_API_KEY", ""),
) as e_client:

    res = e_client.yelp.get_business(request={
        "business_id": "<id>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `request`                                                               | [models.GetBusinessRequestBody](../../models/getbusinessrequestbody.md) | :heavy_check_mark:                                                      | The request object to use for the request.                              |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[models.GetBusinessResponseBody](../../models/getbusinessresponsebody.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.UserError   | 400                | application/json   |
| models.ServerError | 500                | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## get_business_reviews

Get a list of reviews on Yelp for a given business ID

### Example Usage

<!-- UsageSnippet language="python" operationID="get-business-reviews" method="post" path="/yelp/get-business-reviews" -->
```python
from exfunc import Exfunc
import os


with Exfunc(
    api_key=os.getenv("EXFUNC_API_KEY", ""),
) as e_client:

    res = e_client.yelp.get_business_reviews(request={
        "business_id": "<id>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `request`                                                                             | [models.GetBusinessReviewsRequestBody](../../models/getbusinessreviewsrequestbody.md) | :heavy_check_mark:                                                                    | The request object to use for the request.                                            |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[models.GetBusinessReviewsResponseBody](../../models/getbusinessreviewsresponsebody.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.UserError   | 400                | application/json   |
| models.ServerError | 500                | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## search_businesses

Search for businesses on Yelp given a query, location, and other criteria

### Example Usage

<!-- UsageSnippet language="python" operationID="search-businesses" method="post" path="/yelp/search-businesses" -->
```python
from exfunc import Exfunc
import os


with Exfunc(
    api_key=os.getenv("EXFUNC_API_KEY", ""),
) as e_client:

    res = e_client.yelp.search_businesses(request={
        "query": "<value>",
        "location": "<value>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `request`                                                                         | [models.SearchBusinessesRequestBody](../../models/searchbusinessesrequestbody.md) | :heavy_check_mark:                                                                | The request object to use for the request.                                        |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.SearchBusinessesResponseBody](../../models/searchbusinessesresponsebody.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.UserError   | 400                | application/json   |
| models.ServerError | 500                | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |