# LinkedInPerson


## Fields

| Field                                                   | Type                                                    | Required                                                | Description                                             |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| `url`                                                   | *Optional[str]*                                         | :heavy_minus_sign:                                      | URL to the person's profile                             |
| `name`                                                  | *Optional[str]*                                         | :heavy_minus_sign:                                      | Full name of the person                                 |
| `location`                                              | *Optional[str]*                                         | :heavy_minus_sign:                                      | Location of the person                                  |
| `title`                                                 | *Optional[str]*                                         | :heavy_minus_sign:                                      | Job title of the person                                 |
| `company_name`                                          | *Optional[str]*                                         | :heavy_minus_sign:                                      | Name of the company the person works for                |
| `company_url`                                           | *Optional[str]*                                         | :heavy_minus_sign:                                      | URL to the company profile                              |
| `experiences`                                           | List[[models.Experiences](../models/experiences.md)]    | :heavy_minus_sign:                                      | List of experiences or previous job roles of the person |