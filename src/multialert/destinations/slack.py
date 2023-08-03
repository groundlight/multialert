from slack_sdk import WebClient

def send_slack(token: str, channel_id: str, body: str):
    """
    Sends a Slack message with the given parameters.

    Parameters
    ----------
    token : str
        The token of the Slack app.
    channel_id : str
        The ID of the channel to send the message to.
    body : str
        The body of the message.
    """
    client = WebClient(token=token)
    response = client.chat_postMessage(
        channel=channel_id,
        text=body
    )