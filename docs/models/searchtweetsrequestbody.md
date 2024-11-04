# SearchTweetsRequestBody


## Fields

| Field                                      | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `query`                                    | *str*                                      | :heavy_check_mark:                         | The search query string                    |
| `type`                                     | [Optional[models.Type]](../models/type.md) | :heavy_minus_sign:                         | The type of search                         |
| `count`                                    | *Optional[int]*                            | :heavy_minus_sign:                         | The number of results to retrieve          |