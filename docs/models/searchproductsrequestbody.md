# SearchProductsRequestBody


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `query`                                                            | *str*                                                              | :heavy_check_mark:                                                 | The search query for products                                      |
| `country_code`                                                     | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | The country code for filtering products                            |
| `page`                                                             | *Optional[int]*                                                    | :heavy_minus_sign:                                                 | Page number for pagination (default is 1)                          |
| `per_page`                                                         | *Optional[int]*                                                    | :heavy_minus_sign:                                                 | Number of products to return per page (default is 10)              |
| `sort_by`                                                          | [Optional[models.SortBy]](../models/sortby.md)                     | :heavy_minus_sign:                                                 | Sort the results by a specific field                               |
| `product_condition`                                                | [Optional[models.ProductCondition]](../models/productcondition.md) | :heavy_minus_sign:                                                 | Filter products by condition                                       |