# SearchPeopleRequestBody


## Fields

| Field                                     | Type                                      | Required                                  | Description                               |
| ----------------------------------------- | ----------------------------------------- | ----------------------------------------- | ----------------------------------------- |
| `keywords`                                | *str*                                     | :heavy_check_mark:                        | Keywords to search for in people profiles |
| `locations`                               | List[*str*]                               | :heavy_minus_sign:                        | N/A                                       |
| `titles`                                  | List[*str*]                               | :heavy_minus_sign:                        | N/A                                       |
| `seniorities`                             | List[*str*]                               | :heavy_minus_sign:                        | N/A                                       |
| `company_sizes`                           | List[*str*]                               | :heavy_minus_sign:                        | N/A                                       |
| `company_industries`                      | List[*str*]                               | :heavy_minus_sign:                        | N/A                                       |
| `company_domains`                         | List[*str*]                               | :heavy_minus_sign:                        | N/A                                       |
| `page`                                    | *Optional[int]*                           | :heavy_minus_sign:                        | Page number for pagination (default is 1) |