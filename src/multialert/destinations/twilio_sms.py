from twilio.rest import Client

def send_sms(body: str, account_sid: str, auth_token: str, sender_number: str, recipient_number: str):
    """
    Sends an SMS with the given parameters.

    Parameters
    ----------
    body : str
        The body of the SMS.
    account_sid : str
        The account SID of the Twilio account.
    auth_token : str
        The auth token of the Twilio account.
    sender_number : str
        The phone number of the sender.
    recipient_number : str
        The phone number of the recipient.
    """
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=body,
        from_=sender_number,
        to=recipient_number
    )