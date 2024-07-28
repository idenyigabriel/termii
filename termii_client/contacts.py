from termii_client.base import TermiiBase
from termii_client.mixins import TermiiPageMixin


class TermiiContact(TermiiPageMixin, TermiiBase):
    """Termii api resources related to contacts

    - public methods
        - list: retrieve list of all contacts in the specified phonebook
        - create: create new contact in a specified phonebook
        - bulk_create: create bulk of new contacts in the specified phonebook
        - delete: delete a specified contact
    """

    __endpoint = "/phonebooks"

    def list(self, phonebook_id: str, pagination_url: str = None) -> dict:
        """Retrieve list of all contacts in the specified phonebook
        - @params
            - phonebook_id: phonebook to list it's contacts.
            - pagination_url (optional): next or previous page url as returned on termii api response
        """
        params = dict()
        params["api_key"] = self._api_key
        params["page"] = self._get_page_number(pagination_url)

        endpoint = f"{self.__endpoint}/{phonebook_id}/contacts"
        return self._get(endpoint, params=params)

    def create(self, phonebook_id: str, payload: dict) -> dict:
        """Create new contact in the specified phonebook
        - @params
            - phonebook_id: phonebook to create contact in.
            - payload: payload as specified on termii documentation, optionally excluding api_key
        """
        payload["api_key"] = payload.get("api_key", self._api_key)

        endpoint = f"{self.__endpoint}/{phonebook_id}/contacts"
        return self._post(endpoint, payload=payload)

    def bulk_create(self, phonebook_id: str, payload: dict) -> dict:
        """Create bulk of new contacts in the specified phonebook
        - @params
            - phonebook_id: phonebook to create contacts in.
            - payload: payload as specified on termii documentation, optionally excluding api_key
        """
        payload["api_key"] = payload.get("api_key", self._api_key)

        endpoint = f"{self.__endpoint}/{phonebook_id}/contacts"
        return self._post(endpoint, payload=payload)

    def delete(self, contact_id: str) -> dict:
        """Delete a specified contact
        - @params
            - contact_id: id of contact to delete
        """
        params = {"api_key": self._api_key}

        endpoint = f"{self.__endpoint}/contact/{contact_id}"
        return self._delete(endpoint, params=params)
