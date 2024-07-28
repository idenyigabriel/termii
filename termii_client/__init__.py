from termii_client.token import TermiiToken
from termii_client.contacts import TermiiContact
from termii_client.insights import TermiiInsights
from termii_client.campaigns import TermiiCampaign
from termii_client.sender_id import TermiiSenderID
from termii_client.messaging import TermiiMessaging
from termii_client.phonebook import TermiiPhonebook


class Termii:
    """
    Termii entry class, allows access to all methods and functionalities on this library.

    @attributes
        - token - access token related processes
        - contacts - access contacts related processes and resources
        - campaigns - access campaign related processes and resources
        - insights - acccess insights related processes and resources
        - sender_id - access sender id related processes and resources
        - phonebooks - access phonebook related processes and resources
        - messaging - access messaging related proceses and resources
    """

    def __init__(self, api_key: str) -> None:
        self.token: TermiiToken = TermiiToken(api_key)
        self.contacts: TermiiContact = TermiiContact(api_key)
        self.campaigns: TermiiCampaign = TermiiCampaign(api_key)
        self.insights: TermiiInsights = TermiiInsights(api_key)
        self.sender_id: TermiiSenderID = TermiiSenderID(api_key)
        self.phonebooks: TermiiPhonebook = TermiiPhonebook(api_key)
        self.messaging: TermiiMessaging = TermiiMessaging(api_key)
