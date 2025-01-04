# GlassdoorSearchJobPostingsRequestBody


## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `query`                                                | *Optional[str]*                                        | :heavy_minus_sign:                                     | The search query for job postings                      |
| `location`                                             | *Optional[str]*                                        | :heavy_minus_sign:                                     | Location to filter job postings                        |
| `date_posted`                                          | [Optional[models.DatePosted]](../models/dateposted.md) | :heavy_minus_sign:                                     | Filter for job postings based on when they were posted |
| `next_token`                                           | *OptionalNullable[str]*                                | :heavy_minus_sign:                                     | Next token for pagination                              |