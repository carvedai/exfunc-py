<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from exfunc import Exfunc
import os

with Exfunc(
    api_key=os.getenv("EXFUNC_API_KEY", ""),
) as s:
    res = s.google.get_product(request={
        "product_id": "<id>",
    })

    if res is not None:
        # handle response
        pass
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
    ) as s:
        res = await s.google.get_product_async(request={
            "product_id": "<id>",
        })

        if res is not None:
            # handle response
            pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->