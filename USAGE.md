<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from exfunc import Exfunc
import os


with Exfunc(
    api_key=os.getenv("EXFUNC_API_KEY", ""),
) as e_client:

    res = e_client.glassdoor.search_job_postings(request={})

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
from exfunc import Exfunc
import os

async def main():

    async with Exfunc(
        api_key=os.getenv("EXFUNC_API_KEY", ""),
    ) as e_client:

        res = await e_client.glassdoor.search_job_postings_async(request={})

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->