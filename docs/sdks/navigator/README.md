# Navigator
(*navigator*)

## Overview

### Available Operations

* [get_task](#get_task) - Get web navigator task results
* [start_task](#start_task) - Start a web navigator task
* [scrape](#scrape) - Scrape a web page

## get_task

Get web navigator task results for a given task ID

### Example Usage

<!-- UsageSnippet language="python" operationID="get-task" method="post" path="/navigator/get-task" -->
```python
from exfunc import Exfunc
import os


with Exfunc(
    api_key=os.getenv("EXFUNC_API_KEY", ""),
) as e_client:

    res = e_client.navigator.get_task(request={
        "task_id": "<id>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.GetTaskRequestBody](../../models/gettaskrequestbody.md)     | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetTaskResponseBody](../../models/gettaskresponsebody.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.UserError   | 400                | application/json   |
| models.ServerError | 500                | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## start_task

Start a web navigator task for a given url and objective

### Example Usage

<!-- UsageSnippet language="python" operationID="start-task" method="post" path="/navigator/start-task" -->
```python
from exfunc import Exfunc
import os


with Exfunc(
    api_key=os.getenv("EXFUNC_API_KEY", ""),
) as e_client:

    res = e_client.navigator.start_task(request={
        "url": "https://great-maestro.name/",
        "objective": "<value>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.StartTaskRequestBody](../../models/starttaskrequestbody.md) | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.StartTaskResponseBody](../../models/starttaskresponsebody.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.UserError   | 400                | application/json   |
| models.ServerError | 500                | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## scrape

Scrape a web page for a given url

### Example Usage

<!-- UsageSnippet language="python" operationID="scrape" method="post" path="/navigator/scrape" -->
```python
from exfunc import Exfunc
import os


with Exfunc(
    api_key=os.getenv("EXFUNC_API_KEY", ""),
) as e_client:

    res = e_client.navigator.scrape(request={
        "url": "https://all-grandpa.net/",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.ScrapeRequestBody](../../models/scraperequestbody.md)       | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ScrapeResponseBody](../../models/scraperesponsebody.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.UserError   | 400                | application/json   |
| models.ServerError | 500                | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |