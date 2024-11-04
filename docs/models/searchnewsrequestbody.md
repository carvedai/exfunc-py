# SearchNewsRequestBody


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `query`                                                      | *str*                                                        | :heavy_check_mark:                                           | The search query for news articles                           |
| `country_code`                                               | *Optional[str]*                                              | :heavy_minus_sign:                                           | The country code for filtering news                          |
| `per_page`                                                   | *Optional[int]*                                              | :heavy_minus_sign:                                           | Number of news articles to return per page (default is 10)   |
| `time_published`                                             | [Optional[models.TimePublished]](../models/timepublished.md) | :heavy_minus_sign:                                           | Filter news articles published after this date               |