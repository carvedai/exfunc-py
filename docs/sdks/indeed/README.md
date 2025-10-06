# Indeed
(*indeed*)

## Overview

### Available Operations

* [search_job_postings](#search_job_postings) - Search job postings on Indeed

## search_job_postings

Search job postings on Indeed for a given query

### Example Usage

<!-- UsageSnippet language="python" operationID="indeed-search-job-postings" method="post" path="/indeed/search-job-postings" -->
```python
from exfunc import Exfunc
import os


with Exfunc(
    api_key=os.getenv("EXFUNC_API_KEY", ""),
) as e_client:

    res = e_client.indeed.search_job_postings(request={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `request`                                                                                       | [models.IndeedSearchJobPostingsRequestBody](../../models/indeedsearchjobpostingsrequestbody.md) | :heavy_check_mark:                                                                              | The request object to use for the request.                                                      |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |

### Response

**[models.IndeedSearchJobPostingsResponseBody](../../models/indeedsearchjobpostingsresponsebody.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.UserError   | 400                | application/json   |
| models.ServerError | 500                | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |