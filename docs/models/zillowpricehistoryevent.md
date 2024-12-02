# ZillowPriceHistoryEvent


## Fields

| Field                                                           | Type                                                            | Required                                                        | Description                                                     |
| --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| `date_posted`                                                   | *Optional[str]*                                                 | :heavy_minus_sign:                                              | The date of the price change                                    |
| `price`                                                         | *OptionalNullable[float]*                                       | :heavy_minus_sign:                                              | The price of the property at the given date                     |
| `time_epoch`                                                    | *Optional[int]*                                                 | :heavy_minus_sign:                                              | Time of the price change in epoch format                        |
| `price_per_square_foot`                                         | *OptionalNullable[float]*                                       | :heavy_minus_sign:                                              | Price per square foot at the given date                         |
| `price_change_rate`                                             | *Optional[float]*                                               | :heavy_minus_sign:                                              | Rate of change in price over time                               |
| `event`                                                         | *Optional[str]*                                                 | :heavy_minus_sign:                                              | Description of the event (e.g., price increase, price decrease) |
| `source`                                                        | *Optional[str]*                                                 | :heavy_minus_sign:                                              | Source of the price history data                                |
| `is_rental`                                                     | *Optional[bool]*                                                | :heavy_minus_sign:                                              | Indicates if the property is a rental                           |