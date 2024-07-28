from termii_client.base import TermiiBase
from termii_client.mixins import TermiiPageMixin


class TermiiInsights(TermiiPageMixin, TermiiBase):
    """Termii api resources related to insights

    - public methods
        - balance: retrieve termii account balance
        - hitory: retrieve reports for messages sent across the sms, voice & whatsapp channels.
        - search: verify phone numbers and automatically detect their status as well as current network.
        - status: verify if a number is fake or has ported to a new network.
    """

    def balance(self) -> dict:
        """Retrieve termii account balance"""

        params = {"api_key": self._api_key}
        return self._get("/get-balance", params=params)

    def history(self, pagination_url: str = None) -> dict:
        """Retrieve reports for messages sent across the sms, voice & whatsapp channels.
        - @params
            - pagination_url (optional): next or previous page url as returned on termii api response
        """
        params = dict()
        params["api_key"] = self._api_key
        params["page"] = self._get_page_number(pagination_url)
        return self._get("/sms/inbox", params=params)

    def search(self, phone_number: str) -> dict:
        """Verify phone numbers and automatically detect their status as well as current network.
        - @params
            - phone_number: phone number to check
        """
        params = {"api_key": self._api_key, "phone_number": phone_number}
        return self._get("/check/dnd", params=params)

    def status(self, phone_number: str, country_code: str) -> dict:
        """Verify if a number is fake or has ported to a new network.
        - @params
            - phone_number: phone number to check
            - country_code: phone number country code eg: NG
        """
        params = dict()
        params["api_key"] = self._api_key
        params["phone_number"] = phone_number
        params["country_code"] = country_code
        return self._get("/insight/number/query", params=params)
