# MultiAlert: Flexibly send various alerts with a unified interface 

MultiAlert is a Python package that provides a unified interface to send various alerts. It is designed to be flexible and extensible. It is also designed to be easy to use.  With MultiAlert you configure your alerts with a YAML block and then send them with a single line of code.

MultiAlert currently supports the following alert types:

* `audio` (plays a pre-recorded sound)
* `voice` (speaks a message through the local speaker)
* `slack` (sends a message to a Slack channel)
* `text`  (prints a message to the console)

Planned alert types include:
* `sms` (sends a text message, using Twilio)
* `email` (sends an email)
* `webhook` (calls a webhook)

## Quick Start

You can install MultiAlert from PyPI with pip:

```bash
pip install multialert
```

And then use it in a Python script:

```python
from multialert import MultiAlert

alerter = MultiAlert(config={
    "type": "voice",
    "opts": {
        "message": "You have been alerted!"
    }
})
alerter.alert()
```

## Configuration and Usage

Initialize the MultiAlert object with a YAML configuration file:

```python
import os

from multialert import MultiAlert

alerter = MultiAlert()
# Note the default is equivalent to:
# MultiAlert(config=os.environ.get("MULTIALERT_CONFIG", "multialert.yaml"))

alerter.alert(message="You have been alerted!")
```


### Explicit Configuration in Python

You can also configure MultiAlert directly in Python:

```python
from multialert import MultiAlert

alerter = MultiAlert(
    config={
        "default": [
            {
                "type": "audio",
                "opts": {
                    "file": "alert.wav"
                }
            },
            {
                "type": "voice",
                "opts": {
                    "message": "You have been alerted!"
                }
            },
            {
                "type": "slack",
                "opts": {
                    "message": "You have been alerted!",
                    "channel": "#alerts",
                    "token": "xoxb-1234567890-123456789012-1234567890-1234567890"
                }
            },
            {
                "type": "text",
                "opts": {
                    "message": "You have been alerted!"
                }
            }
        ]
    }
)
```
