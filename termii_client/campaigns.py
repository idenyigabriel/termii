from termii_client.base import TermiiBase
from termii_client.mixins import TermiiPageMixin


class TermiiCampaign(TermiiPageMixin, TermiiBase):
    """Termii api resources related to campaigns

    - public methods:
        - send: for sending a campaign
        - list: for lisitng all campaigns
        - history: for listing the history of a specific campaign
    """

    def send(self, payload: dict) -> dict:
        """
        Send a campaign
        - @params:
            - payload - as specified on termii documentation, optionally excluding api_key
        """
        payload["api_key"] = payload.get("api_key", self._api_key)
        return self._post("/sms/campaigns/send", payload=payload)

    def list(self, pagination_url: str = None) -> dict:
        """
        Retrieve list of all campaigns
        - @params:
            - pagination_url (optional): next or previous page url as returned on termii api response
        """
        params = dict()
        params["api_key"] = self._api_key
        params["page"] = self._get_page_number(pagination_url)
        return self._get("/sms/campaigns", params=params)

    def history(self, campaign_id: str, pagination_url: str = None) -> dict:
        """
        Retrieve history for specified campaign
        - @params
            - campaign_id: campaign id to retrieve it's history
            - pagination_url (optional): next or previous page url as returned on termii api response
        """
        params = dict()
        params["api_key"] = self._api_key
        params["page"] = self._get_page_number(pagination_url)
        return self._get("/sms/campaigns/" + str(campaign_id), params=params)
