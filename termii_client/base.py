import requests


class TermiiBase:
    """
    Termi base class, this is inherited by all concrete classes

    @params
        - api_key - Termii account api key, find on termii dashboard

    @protected methods
        - _get - handles get requests to termii api
        - _post - handles post requests to termii api
        - _patch - handles patch requests to termii api
        - _delete - handles delete requests to termii api
    """

    __base_url = "https://api.ng.termii.com/api"
    __headers = {"Content-Type": "application/json"}

    def __init__(self, api_key: str) -> None:
        self._api_key = api_key

    def _post(self, endpoint: str, params: dict = None, payload: dict = None) -> dict:
        url = self.__base_url + endpoint
        response = requests.post(
            url, params=params, json=payload, headers=self.__headers
        )
        return response.json()

    def _get(self, endpoint: str, params: dict = None, payload: dict = None) -> dict:
        url = self.__base_url + endpoint
        data = requests.get(url, json=payload, params=params, headers=self.__headers)
        return data.json()

    def _patch(self, endpoint: str, params: dict = None, payload: dict = None) -> dict:
        url = self.__base_url + endpoint
        response = requests.patch(
            url, json=payload, params=params, headers=self.__headers
        )
        return response.json()

    def _delete(self, endpoint: str, params: dict = None, payload: dict = None) -> dict:
        url = self.__base_url + endpoint
        response = requests.delete(
            url, json=payload, params=params, headers=self.__headers
        )
        return response.json()
