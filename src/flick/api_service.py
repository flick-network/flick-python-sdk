""" Module for initializing request class """
import urllib
import requests


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


class FlickAPI(requests.Session):
    """Base class for making all requsts to flick.network"""

    SANDBOX_BASE_URL = "https://sandbox-api.flick.network"
    PRODUCTION_BASE_URL = "https://api.flick.network"

    def get_base_url(self):
        """ Get the base url for making requests """

        if self.custom_config.environment == Config.PRODUCTION:
            return self.PRODUCTION_BASE_URL

        return self.SANDBOX_BASE_URL



    def __init__(self, *args, config: Config, **kwargs):
        """
        Customised requests.Session class for common base url

        Args:
            url_base (string, optional): base url for all web requests . Defaults to None.
        """

        self.custom_config = config
        super(FlickAPI, self).__init__(*args, **kwargs)
        self.url_base = self.get_base_url()



    def request(self, method, url,
                params=None,
                data=None,
                headers=None,
                cookies=None,
                files=None,
                auth=None,
                timeout=None,
                allow_redirects=True,
                proxies=None,
                hooks=None,
                stream=None,
                verify=None,
                cert=None,
                json=None,):
        """concatenate and create all relavent urls

        Args:
            method (str): HTTP Method
            url (str): Remaining part of URL

        Returns:
            requests: requests object to use 
        """
        modified_url = urllib.parse.urljoin(base=self.url_base, url=url)

        if headers is not None:
            headers["Authorization"] =  f"Bearer {self.custom_config.api_key}",
        else:
            headers = {
                "Authorization": f"Bearer {self.custom_config.api_key}",
            }

        return super(FlickAPI, self).request(method, modified_url, params,
                                                   data,
                                                   headers,
                                                   cookies,
                                                   files,
                                                   auth,
                                                   timeout,
                                                   allow_redirects,
                                                   proxies,
                                                   hooks,
                                                   stream,
                                                   verify,
                                                   cert,
                                                   json)
