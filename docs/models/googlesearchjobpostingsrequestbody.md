# GoogleSearchJobPostingsRequestBody


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `query`                                                    | *str*                                                      | :heavy_check_mark:                                         | The search query for job postings                          |
| `location`                                                 | *Optional[str]*                                            | :heavy_minus_sign:                                         | Location to filter job postings                            |
| `country_code`                                             | *Optional[str]*                                            | :heavy_minus_sign:                                         | The country code to filter job postings                    |
| `date_posted`                                              | [Optional[models.DatePosted]](../models/dateposted.md)     | :heavy_minus_sign:                                         | Filter for job postings based on when they were posted     |
| `job_types`                                                | List[[models.JobTypes](../models/jobtypes.md)]             | :heavy_minus_sign:                                         | Job types to filter (e.g., Full-time, Part-time)           |
| `page`                                                     | *Optional[int]*                                            | :heavy_minus_sign:                                         | Page number for pagination (default is 1)                  |
| `per_page`                                                 | *Optional[int]*                                            | :heavy_minus_sign:                                         | Number of news articles to return per page (default is 10) |