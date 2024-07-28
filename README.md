<p align="center">
    <img title="Flutterwave" height="100" src="https://developer.termii.com/termii-logo.svg" width="30%" />
</p>

# Termii Python Library.

## Introduction

The python library provides easy access to `Termii` API for Python users. Accelerate development with our Python library by abstracting `Termii` API complexities and providing easy-to-use functions.

Please see [the docs](https://developer.termii.com/) for the most up-to-date documentation of `Termii` API.

Available features include:
- Campaigns: send, list and history
- Contacts: list, create(single/bulk) and delete
- Insights: balance, history, search and status
- Messaging: sms(single/bulk), template api, number api
- Phonebooks: list, create, update and delete
- SenderID: list, request
- Token: voice_call, voice_token, email_token, send, in_app, verify

## Table of Contents

1. [Requirements](#requirements)
2. [Installation](#installation)
3. [Initialization](#initialization)
4. [Usage](#usage)
6. [Debugging](#debugging)
7. [Support](#support)
8. [Contribution Guidelines](#contributing)
9. [License](#license)

<a name="requirements"></a>
## Requirements

1. Termii API Keys
2. Supported Python versions: >3.8

<a name="installation"></a>
## Installation

To install this library (preferably in an active virtual environment) simply run

```sh
pip3 install termii
```

<a name="initialization"></a>
## Initialization

Import entry class for this package from termii_client.

```py
from termii_client import Termii
```

With this you have access to all the features this library has to offer.
To initialize the library simply create a `Termii` object, while supplying the api key, you can find one in your `Termii` dashboard.

```
termii = Termii("Your API Key")
```

<a name="usage"></a>
## Usage

This is a documentation for all components on termii_client 

> **Note:**
> For convenience, this library will automatically populate the field ```api_key``` using the value specified during initialization.
> for every payload where it is required, but not provided.

### ```termii.campaigns```

This is used for handling all campaign related resources on termii.

Functions included are:

- ```.send```
- ```.list```
- ```.history```


#### ```.send(payload):```
Send a campaign. The payload is a dictionary containing campaign information, optionally excluding api_key.

- ```payload```
    - ```api_key (optional)```
    - ```country_code```
    - ```sender_id```
    - ```message```
    - ```channel```
    - ```message_type```
    - ```phonebook_id```
    - ```campaign_type```
    - ```schedule_sms_status```
    - ```schedule_time```

#### ```.list(pagination_url)```
Retrieve list of all campaigns.

- ```pagination_url (optional)```: In order to transverse through pages (if any), simply pass the next or previous page url as the keyword argument pagination_url.


#### ```.history(campaign_id, pagination_url)```
Retrieve history for specified campaign.

- ```campaign_id```: campaign id to retrieve it's history
- ```pagination_url (optional)```: In order to transverse through pages (if any), simply pass the next or previous page url as the keyword argument pagination_url.

<br />

### ```termii.contacts```

This is used for handling contacts in termii phonebooks.

Functions included are:

- ```.list```
- ```.create```
- ```.create_bulk```
- ```.delete```

#### ```.list(phonebook_id, pagination_url):```
Retrieve list of all contacts in the specified phonebook.

- ```phonebook_id```: phone book id to retrieve it's contacts
- ```pagination_url (optional)```: In order to transverse through pages (if any), simply pass the next or previous page url as the keyword argument pagination_url.


#### ```.create(phonebook_id, payload):```
Create new contact in the specified phonebook

- ```phonebook_id```: phone book id to create contact on.
- ```payload```
    - ```api_key (optional)```
    - ```phone_number```
    - ```country_code```
    - ```email_address```
    - ```first_name```
    - ```last_name```
    - ```company```


#### ```.create_bulk(phonebook_id, payload):```
Create bulk of new contacts in the specified phonebook

- ```phonebook_id```: phone book id to create contact on.
- ```payload```
    - ```api_key (optional)```
    - ```contact_file```
    - ```country_code```


#### ```.delete(contact_id):```
Delete a specified contact

- ```contact_id```: id of contact to delete

<br />

### ```termii.insights```

This is used for handling resources related to insights

Functions included are:

- ```.balance```
- ```.history```
- ```.search```
- ```.status```

#### ```.balance():```
Retrieve termii account balance

#### ```.history(pagination_url):```
Retrieve reports for messages sent across the sms, voice & whatsapp channels.

- ```pagination_url (optional)```: In order to transverse through pages (if any), simply pass the next or previous page url as the keyword argument pagination_url.


#### ```.search(phone_number):```
Verify phone numbers and automatically detect their status as well as current network.

- ```phone_number```: phone number to detect status and current network


#### ```.status(phone_number, country_code):```
Verify if a number is fake or has ported to a new network.

- ```phone_number```: phone number to fake and ported status
- ```country_code```: phone number country code

<br />

### ```termii.messaging```

This is used for handling resources related to Messaging/SMS

Functions included are:

- ```.send```
- ```.send_bulk```
- ```.send_auto_message```
- ```.send_template_message```

#### ```.send_single(payload):```
Send single sms on termii api

- ```payload```
    - ```api_key (0ptional)```
    - ```to```
    - ```from```
    - ```sms```
    - ```type```
    - ```channel```
    - ```media (Optional Dict)```
        - ```url```
        - ```caption```

#### ```.send_bulk(payload):```
Send bulk sms on termii api

- ```payload```
    - ```api_key (0ptional)```
    - ```to```
    - ```from```
    - ```sms```
    - ```type```
    - ```channel```

#### ```.send_auto_message(payload):```
Send single sms on termii api with auto generated numbers

- ```payload```
    - ```api_key (0ptional)```
    - ```to```
    - ```from```

#### ```.send_template_message(payload):```
Set a template for the one-time-passwords (pins) sent to their customers via whatsapp or sms.

- ```payload```
    - ```api_key (0ptional)```
    - ```phone_number```
    - ```device_id```
    - ```template_id```
    - ```data```

<br />

### ```termii.phonebooks```

This is used for handling all phonebook related resources on termii.

Functions included are:

- ```.list```
- ```.create```
- ```.update```
- ```.delete```


#### ```.list(pagination_url)```
Retrieve list of all phonebooks

- ```pagination_url (optional)```: In order to transverse through pages (if any), simply pass the next or previous page url as the keyword argument pagination_url.

#### ```.create(phonebook_name, description)```
Retrieve list of all phonebooks

- ```phonebook_name```
- ```description (optional)```

#### ```.update(phonebook_id, phonebook_name)```
Update existing phonebook

- ```phonebook_id```: Phonebook ID to update
- ```phonebook_name```: New phonebook name

#### ```.delete(phonebook_id)```
Delete existing phonebook

- ```phonebook_id```: Phonebook ID to delete

<br />

### ```termii.sender_id```

This is used for handling all phonebook related resources on termii.

Functions included are:

- ```.list```
- ```.request```


#### ```.list(pagination_url)```
Retrieve list of all sender ID's

- ```pagination_url (optional)```: In order to transverse through pages (if any), simply pass the next or previous page url as the keyword argument pagination_url.

#### ```.request(sender_id, usecase, company)```
Request for a sender id

- ```sender_id```: sender id being requested eg: CompanyName
- ```usecase```: a sample of the type of message to be sent.
- ```company```: name of the company with the sender ID

<br />

### ```termii.token```

This is used for handling all phonebook related resources on termii.

Functions included are:

- ```.voice_call```
- ```.email_token```
- ```.in_app```
- ```.send```
- ```.verify```
- ```.voice_token```


#### ```.voice_call(payload)```
Send messages from your application through our voice channel to a phone number.

- ```payload```
    - ```api_key (Optional)```
    - ```phone_number```
    - ```code```


#### ```.email_token(payload)```
Send one-time-passwords from your application through our email channel to an email address.

- ```payload```
    - ```api_key (Optional)```
    - ```email_address```
    - ```code```
    - ```email_configuration_id```


#### ```.in_app(payload)```
Returns OTP codes in JSON format which can be used within any web or mobile app.

- ```payload```
    - ```api_key (Optional)```
    - ```phone_number```
    - ```pin_attempts```
    - ```pin_time_to_live```
    - ```pin_length```


#### ```.send(payload)```
Send one-time-passwords (OTP) across any available messaging channel on Termii

- ```payload```
    - ```api_key (Optional)```
    - ```message_type```
    - ```to```
    - ```from```
    - ```channel```
    - ```pin_attempts```
    - ```pin_time_to_live```
    - ```pin_length```
    - ```pin_placeholder```
    - ```message_text```


#### ```.verify(payload)```
Check status of tokens sent to customers.

- ```payload```
    - ```api_key (Optional)```
    - ```pin_id```
    - ```pin```


#### ```.voice_token(payload)```
Generate and trigger one-time passwords (OTP) through the voice channel to a phone number.

- ```payload```
    - ```api_key (Optional)```
    - ```phone_number```
    - ```pin_attempts```
    - ```pin_time_to_live```
    - ```pin_length```


<a name="debugging"></a>
## Debugging Errors

I understand that you may run into some errors while integrating this library. Please open discussion on any problems you may have about this library

For authorization and validation error responses, double-check your API keys and request. If you get a server error, kindly engage the Termii for support @+234-8137751523.

<a name="support"></a>
## Support

For additional assistance using this library, feel free to reach out, i'll be looking forward to it.

You can also follow me on [twitter](https://x.com/idenyigabriel) and [github](https://github.com/idenyigabriel) and [linkedin](https://www.linkedin.com/in/gabriel-idenyi/). 😊.


<a name="license"></a>
## License

By contributing to this library, you agree that your contributions will be licensed under its MIT license.


<a name="contributing"></a>
## Contribution guidelines

Read more about our community contribution guidelines [here](./CONTRIBUTING.md)
