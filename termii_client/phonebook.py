from termii_client.base import TermiiBase
from termii_client.mixins import TermiiPageMixin


class TermiiPhonebook(TermiiPageMixin, TermiiBase):
    """
    Handles termii api resources related to phonebooks

    @methods
        - list: retrieve list of all phonebooks
        - create: create new phonebook
        - update: update existing phonebook
        - delete: delete existing phonebook
    """

    __endpoint = "/phonebooks"

    def list(self, pagination_url: str = None) -> dict:
        """Retrieve list of all phonebooks
        - @params
            - pagination_url (optional): next or previous page url as returned on termii api response
        """
        params = dict()
        params["api_key"] = self._api_key
        params["page"] = self._get_page_number(pagination_url)

        return self._get(self.__endpoint, params=params)

    def create(self, phonebook_name: str, description: str = None) -> dict:
        """Create new phonebook
        - @params
            - phonebook_name: name of phone being created
            - description (optional): a brief description of what phonebook is about.
        """
        payload = dict()
        payload["api_key"] = self._api_key
        payload["phonebook_name"] = phonebook_name
        payload["description"] = description

        return self._post(self.__endpoint, payload=payload)

    def update(self, phonebook_id: str, phonebook_name: str) -> dict:
        """Update existing phonebook
        - @params
            - phonebook_id: id of phonebook to be updated
            - phonebook_name: new name to assign to phone book.
        """
        payload = dict()
        payload["api_key"] = self._api_key
        payload["phonebook_name"] = phonebook_name

        endpoint = f"{self.__endpoint}/{phonebook_id}"
        return self._patch(endpoint, payload=payload)

    def delete(self, phonebook_id: str) -> dict:
        """Delete existing phonebook
        - @params
            - phonebook_id: id of phonebook to be deleted
        """
        params = {"api_key": self._api_key}

        endpoint = f"{self.__endpoint}/{phonebook_id}"
        return self._delete(endpoint, params=params)
