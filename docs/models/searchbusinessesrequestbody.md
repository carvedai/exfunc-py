# SearchBusinessesRequestBody


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `query`                                                                        | *str*                                                                          | :heavy_check_mark:                                                             | The search term to find businesses                                             |
| `location`                                                                     | *str*                                                                          | :heavy_check_mark:                                                             | The location to search for businesses                                          |
| `sort_by`                                                                      | [Optional[models.SearchBusinessesSortBy]](../models/searchbusinessessortby.md) | :heavy_minus_sign:                                                             | The criteria to sort the results (e.g., "recommended", "highest_rated", etc.)  |
| `start`                                                                        | *Optional[int]*                                                                | :heavy_minus_sign:                                                             | The starting index for pagination (default is 0)                               |