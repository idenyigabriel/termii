from termii_client.base import TermiiBase
from termii_client.mixins import TermiiPageMixin


class TermiiSenderID(TermiiPageMixin, TermiiBase):
    """
    Handles termii api resources related to sender id

    @methods
        - list: retrieve list of all sender ID's
        - request: request for a sender id.
    """

    __base_endpoint = "/sender-id"

    def list(self, pagination_url: str = None) -> dict:
        """Retrieve list of all sender ID's
        - @params
            - pagination_url (optional): next or previous page url as returned on termii api response
        """
        params = dict()
        params["api_key"] = self._api_key
        params["page"] = self._get_page_number(pagination_url)

        return self._get(self.__base_endpoint, params=params)

    def request(self, sender_id: str, usecase: str, company: str) -> dict:
        """Request for a sender id
        - @params
            - sender_id - sender id being requested eg: CompanyName
            - usecase - a sample of the type of message to be sent.
            - company - name of the company with the sender ID
        """
        payload = dict()
        payload["usecase"] = usecase
        payload["company"] = company
        payload["sender_id"] = sender_id
        payload["api_key"] = self._api_key

        endpoint = f"{self.__base_endpoint}/request"
        return self._post(endpoint, payload=payload)
