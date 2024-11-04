# Tweet


## Fields

| Field                                         | Type                                          | Required                                      | Description                                   |
| --------------------------------------------- | --------------------------------------------- | --------------------------------------------- | --------------------------------------------- |
| `tweet_id`                                    | *Optional[str]*                               | :heavy_minus_sign:                            | Unique identifier for the tweet               |
| `full_text`                                   | *Optional[str]*                               | :heavy_minus_sign:                            | The full text of the tweet                    |
| `created_at`                                  | *Optional[str]*                               | :heavy_minus_sign:                            | The timestamp when the tweet was created      |
| `author_user_id`                              | *Optional[str]*                               | :heavy_minus_sign:                            | The ID of the user who authored the tweet     |
| `bookmark_count`                              | *Optional[int]*                               | :heavy_minus_sign:                            | Number of times the tweet has been bookmarked |
| `reply_count`                                 | *Optional[int]*                               | :heavy_minus_sign:                            | Number of replies to the tweet                |
| `retweet_count`                               | *Optional[int]*                               | :heavy_minus_sign:                            | Number of times the tweet has been retweeted  |
| `retweeted`                                   | *Optional[bool]*                              | :heavy_minus_sign:                            | Indicates if the tweet is a retweet           |
| `urls`                                        | List[*str*]                                   | :heavy_minus_sign:                            | List of URLs included in the tweet            |