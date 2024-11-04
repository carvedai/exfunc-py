# GetProductReviewsRequestBody


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `product_id`                                         | *str*                                                | :heavy_check_mark:                                   | The ID of the product for which to retrieve reviews  |
| `country_code`                                       | *Optional[str]*                                      | :heavy_minus_sign:                                   | The country code for the reviews                     |
| `per_page`                                           | *Optional[int]*                                      | :heavy_minus_sign:                                   | Number of reviews to return per page (default is 10) |