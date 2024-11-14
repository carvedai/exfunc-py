# SearchRoundtripRequestBody


## Fields

| Field                                                                                    | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `origin`                                                                                 | *str*                                                                                    | :heavy_check_mark:                                                                       | The origin location of the itinerary                                                     |
| `destination`                                                                            | *str*                                                                                    | :heavy_check_mark:                                                                       | The destination location of the itinerary                                                |
| `depart_date`                                                                            | *str*                                                                                    | :heavy_check_mark:                                                                       | The departure date of the itinerary. The format has to be YYYY-MM-DD                     |
| `return_date`                                                                            | *str*                                                                                    | :heavy_check_mark:                                                                       | The return date of the itinerary. The format has to be YYYY-MM-DD                        |
| `stops`                                                                                  | List[[models.SearchRoundtripStops](../models/searchroundtripstops.md)]                   | :heavy_minus_sign:                                                                       | The list of filter values for number of stops                                            |
| `num_adults`                                                                             | *Optional[float]*                                                                        | :heavy_minus_sign:                                                                       | The number of adults for the itinerary                                                   |
| `num_children`                                                                           | *Optional[float]*                                                                        | :heavy_minus_sign:                                                                       | The number of children for the itinerary                                                 |
| `num_infants`                                                                            | *Optional[float]*                                                                        | :heavy_minus_sign:                                                                       | The number of infants for the itinerary                                                  |
| `cabin_class`                                                                            | [Optional[models.SearchRoundtripCabinClass]](../models/searchroundtripcabinclass.md)     | :heavy_minus_sign:                                                                       | The cabin class filter                                                                   |
| `include_origin_nearby_airports`                                                         | *Optional[bool]*                                                                         | :heavy_minus_sign:                                                                       | Boolean to indicate whether to include nearby origin airports in the results or not      |
| `include_destination_nearby_airports`                                                    | *Optional[bool]*                                                                         | :heavy_minus_sign:                                                                       | Boolean to indicate whether to include nearby destination airports in the results or not |