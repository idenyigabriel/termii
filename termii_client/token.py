from termii_client.base import TermiiBase


class TermiiToken(TermiiBase):
    """Termii api resources related to messaging/sms

    - public methods
        - voice_call: send messages from your application through our voice channel to a phone number.
        - email_token: send one-time-passwords from your application through our email channel to an email address
        - in_app: returns OTP codes in JSON format which can be used within any web or mobile app.
        - voice_token:  generate and trigger one-time passwords (OTP) through the voice channel to a phone number
        - verify: check status of tokens sent to customers.
        - send: send one-time-passwords (OTP) across any available messaging channel on Termii
    """

    def voice_call(self, payload: dict) -> dict:
        """Send messages from your application through our voice channel to a phone number.
        - @params:
            - payload: as specified on termii documentation, optionally excluding api_key
        """
        payload["api_key"] = payload.get("api_key", self._api_key)
        return self._post("/sms/otp/call", payload)

    def email_token(self, payload: dict) -> dict:
        """Send one-time-passwords from your application through our email channel to an email address.
        - @params:
            - payload: as specified on termii documentation, optionally excluding api_key
        """
        payload["api_key"] = payload.get("api_key", self._api_key)
        return self._post("/email/otp/send", payload)

    def in_app(self, payload: dict) -> dict:
        """Returns OTP codes in JSON format which can be used within any web or mobile app.

        - @params:
            - payload: as specified on termii documentation, optionally excluding api_key
        """
        payload["api_key"] = payload.get("api_key", self._api_key)
        return self._post("/sms/otp/generate", payload)

    def voice_token(self, payload: dict) -> dict:
        """Generate and trigger one-time passwords (OTP) through the voice channel to a phone number.
        - @params:
            - payload: as specified on termii documentation, optionally excluding api_key.
        """
        payload["api_key"] = payload.get("api_key", self._api_key)
        return self._post("/sms/otp/send/voice", payload)

    def verify(self, payload: dict) -> dict:
        """Check status of tokens sent to customers.
        - @params:
            - payload: as specified on termii documentation, optionally excluding api_key and from.
        """
        payload["api_key"] = payload.get("api_key", self._api_key)
        return self._post("/sms/otp/verify", payload)

    def send(self, payload: dict) -> dict:
        """Send one-time-passwords (OTP) across any available messaging channel on Termii
        - @params:
            - payload: as specified on termii documentation, optionally excluding api_key
        """
        payload["api_key"] = payload.get("api_key", self._api_key)
        return self._post("/sms/otp/send", payload)
