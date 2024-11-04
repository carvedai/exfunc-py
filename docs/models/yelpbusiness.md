# YelpBusiness


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `business_id`                                        | *Optional[str]*                                      | :heavy_minus_sign:                                   | Unique identifier for the business                   |
| `alias`                                              | *Optional[str]*                                      | :heavy_minus_sign:                                   | A unique identifier used in the URL for the business |
| `name`                                               | *Optional[str]*                                      | :heavy_minus_sign:                                   | The name of the business                             |
| `address`                                            | *Optional[str]*                                      | :heavy_minus_sign:                                   | The physical address of the business                 |
| `website`                                            | *Optional[str]*                                      | :heavy_minus_sign:                                   | The website URL of the business                      |
| `business_page_link`                                 | *Optional[str]*                                      | :heavy_minus_sign:                                   | The link to the business's page on the platform      |
| `categories`                                         | List[[models.Categories](../models/categories.md)]   | :heavy_minus_sign:                                   | List of categories that the business falls under     |
| `rating`                                             | *Optional[float]*                                    | :heavy_minus_sign:                                   | Average rating of the business                       |
| `review_count`                                       | *Optional[int]*                                      | :heavy_minus_sign:                                   | Total number of reviews for the business             |
| `highlights`                                         | List[*str*]                                          | :heavy_minus_sign:                                   | Highlights or features of the business               |
| `service_area`                                       | *Optional[str]*                                      | :heavy_minus_sign:                                   | The area where the business provides services        |
| `neighborhoods`                                      | List[*str*]                                          | :heavy_minus_sign:                                   | List of neighborhoods where the business is located  |