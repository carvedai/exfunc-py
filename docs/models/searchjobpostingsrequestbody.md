# SearchJobPostingsRequestBody


## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `keywords`                                             | *str*                                                  | :heavy_check_mark:                                     | Keywords to search for in job postings                 |
| `location`                                             | *str*                                                  | :heavy_check_mark:                                     | Location to filter job postings                        |
| `date_posted`                                          | [Optional[models.DatePosted]](../models/dateposted.md) | :heavy_minus_sign:                                     | Filter for job postings based on when they were posted |
| `salary`                                               | [Optional[models.Salary]](../models/salary.md)         | :heavy_minus_sign:                                     | Salary range to filter job postings                    |
| `job_types`                                            | List[[models.JobTypes](../models/jobtypes.md)]         | :heavy_minus_sign:                                     | N/A                                                    |
| `work_types`                                           | List[[models.WorkTypes](../models/worktypes.md)]       | :heavy_minus_sign:                                     | N/A                                                    |
| `company_uids`                                         | List[*str*]                                            | :heavy_minus_sign:                                     | N/A                                                    |
| `page`                                                 | *Optional[int]*                                        | :heavy_minus_sign:                                     | Page number for pagination (default is 1)              |