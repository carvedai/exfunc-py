# GoogleNews


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `title`                                                              | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | The title of the news article                                        |
| `link`                                                               | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | The URL link to the news article                                     |
| `snippet`                                                            | *OptionalNullable[str]*                                              | :heavy_minus_sign:                                                   | A brief snippet or summary of the news article                       |
| `photo_url`                                                          | *OptionalNullable[str]*                                              | :heavy_minus_sign:                                                   | The URL of the photo associated with the news article                |
| `published_datetime_utc`                                             | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | The publication date and time in UTC                                 |
| `source_url`                                                         | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | The URL of the source website                                        |
| `source_name`                                                        | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | The name of the news source                                          |