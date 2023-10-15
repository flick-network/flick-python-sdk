""" Module for initializing request class """
import urllib
import aiohttp


class InvalidEnvironmentException(Exception):
    """ For raising invalid environment exceptions """


class Config():

    """ Config class for passing the api key and selecting between  """

    SANDBOX = 'sandbox'
    PRODUCTION = 'production'

    def __init__(self, environment: str, api_key: str) -> None:
        if environment == self.SANDBOX or environment == self.PRODUCTION:
            self.environment = environment
            self.api_key = api_key
        else:
            raise InvalidEnvironmentException(
                "Invalid environment type. use 'sandbox' or 'production'")


class FlickAPI(aiohttp.ClientSession):
    """
    A custom aiohttp client session for making authenticated requests to a specified base URL.

    Args:
        config (Config): The configuration object containing API key and other settings.

    Attributes:
        custom_config (Config): The custom configuration object.
        base_url (str): The base URL for requests.
    """
    SANDBOX_BASE_URL = "https://sandbox-api.flick.network"
    PRODUCTION_BASE_URL = "https://api.flick.network"

    def get_base_url(self):
        """ Get the base url for making requests """

        if self.custom_config.environment == Config.PRODUCTION:
            return self.PRODUCTION_BASE_URL

        return self.SANDBOX_BASE_URL


   

    def __init__(self, config: Config):
        """
        Initialize the CustomSession with a custom configuration.

        Args:
            config (Config): The configuration object containing API key and other settings.
        """
        self.custom_config = config
        super().__init__(headers={'Authorization': f'Bearer {config.api_key}'})
        self.base_url = self.get_base_url()

    def request(self, method, url, **kwargs):
        """
        Make a request using the specified method, URL, and additional keyword arguments.

        Args:
            method (str): The HTTP method for the request (e.g., 'GET', 'POST').
            url (str): The path of the URL to request, relative to the base URL.
            **kwargs: Additional keyword arguments for the request.

        Returns:
            aiohttp.ClientResponse: The response from the request.
        """
        # Prepend the base_url to the request URL
        full_url = urllib.parse.urljoin(base=self.base_url, url=url)
        return super().request(method, full_url, **kwargs)
    