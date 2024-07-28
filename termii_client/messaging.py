from termii_client.base import TermiiBase
from termii_client.mixins import TermiiPageMixin


class TermiiMessaging(TermiiPageMixin, TermiiBase):
    """Termii api resources related to messaging/sms

    - public methods
        - send: send single sms on termii api
        - send_bulk: send bulk sms on termii api
        - send_template_message:  set a template for the one-time-passwords (pins) sent to their customers via whatsapp or sms.
        - send_auto_message: end single sms on termii api with auto generated numbers
    """

    def send(self, payload: dict) -> dict:
        """Send single sms on termii api
        - @params
            - payload: as specified on termii documentation, optionally excluding api_key.
        """
        payload["api_key"] = payload.get("api_key", self._api_key)
        return self._post("/sms/send", payload=payload)

    def send_bulk(self, payload: dict) -> dict:
        """Send bulk sms on termii api
        - @params
            - payload: as specified on termii documentation, optionally excluding api_key.
        """
        payload["api_key"] = payload.get("api_key", self._api_key)
        return self._post("/sms/send/bulk", payload=payload)

    def send_template_message(self, payload: dict) -> dict:
        """Set a template for the one-time-passwords (pins) sent to their customers via whatsapp or sms.
        - @params
            - payload: as specified on termii documentation, optionally excluding api_key to use initialization values
        """
        payload["api_key"] = payload.get("api_key", self._api_key)
        return self._post("/send/template", payload=payload)

    def send_auto_message(self, payload: dict) -> dict:
        """Send single sms on termii api with auto generated numbers
        - @params
            - payload: as specified on termii documentation, optionally excluding api_key.
        """
        payload["api_key"] = payload.get("api_key", self._api_key)
        return self._post("/sms/number/send", payload=payload)
