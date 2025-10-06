# Twitter
(*twitter*)

## Overview

### Available Operations

* [get_tweet](#get_tweet) - Get a tweet by ID
* [get_user](#get_user) - Get a Twitter user by either user ID or username
* [get_user_followers](#get_user_followers) - Get a Twitter user's followers by username
* [get_user_followings](#get_user_followings) - Get a Twitter user's followings by username
* [get_user_tweets](#get_user_tweets) - Get a Twitter user's tweets by username
* [search_tweets](#search_tweets) - Search Twitter for tweets
* [search_users](#search_users) - Search Twitter for users

## get_tweet

Get tweet details given a tweet ID

### Example Usage

<!-- UsageSnippet language="python" operationID="get-tweet" method="post" path="/twitter/get-tweet" -->
```python
from exfunc import Exfunc
import os


with Exfunc(
    api_key=os.getenv("EXFUNC_API_KEY", ""),
) as e_client:

    res = e_client.twitter.get_tweet(request={
        "tweet_id": "<id>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.GetTweetRequestBody](../../models/gettweetrequestbody.md)   | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetTweetResponseBody](../../models/gettweetresponsebody.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.UserError   | 400                | application/json   |
| models.ServerError | 500                | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## get_user

Get user details given a Twitter user ID or username (handle)

### Example Usage

<!-- UsageSnippet language="python" operationID="get-user" method="post" path="/twitter/get-user" -->
```python
from exfunc import Exfunc
import os


with Exfunc(
    api_key=os.getenv("EXFUNC_API_KEY", ""),
) as e_client:

    res = e_client.twitter.get_user(request={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.GetUserRequestBody](../../models/getuserrequestbody.md)     | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetUserResponseBody](../../models/getuserresponsebody.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.UserError   | 400                | application/json   |
| models.ServerError | 500                | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## get_user_followers

Get a list of followers given a Twitter username (handle)

### Example Usage

<!-- UsageSnippet language="python" operationID="get-user-followers" method="post" path="/twitter/get-user-followers" -->
```python
from exfunc import Exfunc
import os


with Exfunc(
    api_key=os.getenv("EXFUNC_API_KEY", ""),
) as e_client:

    res = e_client.twitter.get_user_followers(request={
        "username": "Angel.OConnell68",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `request`                                                                         | [models.GetUserFollowersRequestBody](../../models/getuserfollowersrequestbody.md) | :heavy_check_mark:                                                                | The request object to use for the request.                                        |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.GetUserFollowersResponseBody](../../models/getuserfollowersresponsebody.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.UserError   | 400                | application/json   |
| models.ServerError | 500                | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## get_user_followings

Get a list of followings given a Twitter username (handle)

### Example Usage

<!-- UsageSnippet language="python" operationID="getUserFollowings" method="post" path="/twitter/get-user-followings" -->
```python
from exfunc import Exfunc
import os


with Exfunc(
    api_key=os.getenv("EXFUNC_API_KEY", ""),
) as e_client:

    res = e_client.twitter.get_user_followings(request={
        "username": "Juvenal26",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `request`                                                                           | [models.GetUserFollowingsRequestBody](../../models/getuserfollowingsrequestbody.md) | :heavy_check_mark:                                                                  | The request object to use for the request.                                          |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.GetUserFollowingsResponseBody](../../models/getuserfollowingsresponsebody.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.UserError   | 400                | application/json   |
| models.ServerError | 500                | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## get_user_tweets

Get a list of tweets given a Twitter username (handle)

### Example Usage

<!-- UsageSnippet language="python" operationID="get-user-tweets" method="post" path="/twitter/get-user-tweets" -->
```python
from exfunc import Exfunc
import os


with Exfunc(
    api_key=os.getenv("EXFUNC_API_KEY", ""),
) as e_client:

    res = e_client.twitter.get_user_tweets(request={
        "username": "Norberto_Cassin29",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `request`                                                                   | [models.GetUserTweetsRequestBody](../../models/getusertweetsrequestbody.md) | :heavy_check_mark:                                                          | The request object to use for the request.                                  |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[models.GetUserTweetsResponseBody](../../models/getusertweetsresponsebody.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.UserError   | 400                | application/json   |
| models.ServerError | 500                | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## search_tweets

Search tweets on Twitter for a given query

### Example Usage

<!-- UsageSnippet language="python" operationID="search-tweets" method="post" path="/twitter/search-tweets" -->
```python
from exfunc import Exfunc
import os


with Exfunc(
    api_key=os.getenv("EXFUNC_API_KEY", ""),
) as e_client:

    res = e_client.twitter.search_tweets(request={
        "query": "<value>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `request`                                                                 | [models.SearchTweetsRequestBody](../../models/searchtweetsrequestbody.md) | :heavy_check_mark:                                                        | The request object to use for the request.                                |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.SearchTweetsResponseBody](../../models/searchtweetsresponsebody.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.UserError   | 400                | application/json   |
| models.ServerError | 500                | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## search_users

Search users on Twitter for a given query

### Example Usage

<!-- UsageSnippet language="python" operationID="search-users" method="post" path="/twitter/search-users" -->
```python
from exfunc import Exfunc
import os


with Exfunc(
    api_key=os.getenv("EXFUNC_API_KEY", ""),
) as e_client:

    res = e_client.twitter.search_users(request={
        "query": "<value>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `request`                                                               | [models.SearchUsersRequestBody](../../models/searchusersrequestbody.md) | :heavy_check_mark:                                                      | The request object to use for the request.                              |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[models.SearchUsersResponseBody](../../models/searchusersresponsebody.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.UserError   | 400                | application/json   |
| models.ServerError | 500                | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |