<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from exfunc import Exfunc
import os

with Exfunc(
    api_key=os.getenv("EXFUNC_API_KEY", ""),
) as exfunc:

    res = exfunc.glassdoor.search_job_postings()

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from exfunc import Exfunc
import os

async def main():
    async with Exfunc(
        api_key=os.getenv("EXFUNC_API_KEY", ""),
    ) as exfunc:

        res = await exfunc.glassdoor.search_job_postings_async()

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->