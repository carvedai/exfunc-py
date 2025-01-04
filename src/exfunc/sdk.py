"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from .httpclient import AsyncHttpClient, HttpClient
from .sdkconfiguration import SDKConfiguration
from .utils.logger import Logger, get_default_logger
from .utils.retries import RetryConfig
from exfunc import models, utils
from exfunc._hooks import SDKHooks
from exfunc.glassdoor import Glassdoor
from exfunc.google import Google
from exfunc.indeed import Indeed
from exfunc.linkedin import Linkedin
from exfunc.navigator import Navigator
from exfunc.skyscanner import Skyscanner
from exfunc.twitter import Twitter
from exfunc.types import OptionalNullable, UNSET
from exfunc.yelp import Yelp
from exfunc.zillow import Zillow
import httpx
from typing import Any, Callable, Dict, Optional, Union


class Exfunc(BaseSDK):
    r"""Exfunc APIs: # Authentication

    Exfunc offers one form of authentication:
    - API Key

    <SecurityDefinitions />

    """

    glassdoor: Glassdoor
    google: Google
    indeed: Indeed
    linkedin: Linkedin
    navigator: Navigator
    skyscanner: Skyscanner
    twitter: Twitter
    yelp: Yelp
    zillow: Zillow

    def __init__(
        self,
        api_key: Optional[Union[Optional[str], Callable[[], Optional[str]]]] = None,
        server_idx: Optional[int] = None,
        server_url: Optional[str] = None,
        url_params: Optional[Dict[str, str]] = None,
        client: Optional[HttpClient] = None,
        async_client: Optional[AsyncHttpClient] = None,
        retry_config: OptionalNullable[RetryConfig] = UNSET,
        timeout_ms: Optional[int] = None,
        debug_logger: Optional[Logger] = None,
    ) -> None:
        r"""Instantiates the SDK configuring it with the provided parameters.

        :param api_key: The api_key required for authentication
        :param server_idx: The index of the server to use for all methods
        :param server_url: The server URL to use for all methods
        :param url_params: Parameters to optionally template the server URL with
        :param client: The HTTP client to use for all synchronous methods
        :param async_client: The Async HTTP client to use for all asynchronous methods
        :param retry_config: The retry configuration to use for all supported methods
        :param timeout_ms: Optional request timeout applied to each operation in milliseconds
        """
        if client is None:
            client = httpx.Client()

        assert issubclass(
            type(client), HttpClient
        ), "The provided client must implement the HttpClient protocol."

        if async_client is None:
            async_client = httpx.AsyncClient()

        if debug_logger is None:
            debug_logger = get_default_logger()

        assert issubclass(
            type(async_client), AsyncHttpClient
        ), "The provided async_client must implement the AsyncHttpClient protocol."

        security: Any = None
        if callable(api_key):
            security = lambda: models.Security(api_key=api_key())  # pylint: disable=unnecessary-lambda-assignment
        else:
            security = models.Security(api_key=api_key)

        if server_url is not None:
            if url_params is not None:
                server_url = utils.template_url(server_url, url_params)

        BaseSDK.__init__(
            self,
            SDKConfiguration(
                client=client,
                async_client=async_client,
                security=security,
                server_url=server_url,
                server_idx=server_idx,
                retry_config=retry_config,
                timeout_ms=timeout_ms,
                debug_logger=debug_logger,
            ),
        )

        hooks = SDKHooks()

        current_server_url, *_ = self.sdk_configuration.get_server_details()
        server_url, self.sdk_configuration.client = hooks.sdk_init(
            current_server_url, self.sdk_configuration.client
        )
        if current_server_url != server_url:
            self.sdk_configuration.server_url = server_url

        # pylint: disable=protected-access
        self.sdk_configuration.__dict__["_hooks"] = hooks

        self._init_sdks()

    def _init_sdks(self):
        self.glassdoor = Glassdoor(self.sdk_configuration)
        self.google = Google(self.sdk_configuration)
        self.indeed = Indeed(self.sdk_configuration)
        self.linkedin = Linkedin(self.sdk_configuration)
        self.navigator = Navigator(self.sdk_configuration)
        self.skyscanner = Skyscanner(self.sdk_configuration)
        self.twitter = Twitter(self.sdk_configuration)
        self.yelp = Yelp(self.sdk_configuration)
        self.zillow = Zillow(self.sdk_configuration)

    def __enter__(self):
        return self

    async def __aenter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.sdk_configuration.client is not None:
            self.sdk_configuration.client.close()

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.sdk_configuration.async_client is not None:
            await self.sdk_configuration.async_client.aclose()
