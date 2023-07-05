# MultiAlert: Flexibly send various alerts with a unified interface 

MultiAlert is a Python package that provides a unified interface to send various alerts. It is designed to be flexible and extensible. It is also designed to be easy to use.  With MultiAlert you configure your alerts with a YAML block and then send them with a single line of code.

MultiAlert currently supports the following alert types:

* Audio (plays a sound)
* Voice (speaks a message through the local speaker)
* Slack (sends a message to a Slack channel)
* Stdout (prints a message to the console)

Planned alert types include:
* SMS (sends a text message, using Twilio)
* Email (sends an email)

## Installation

MultiAlert is available on PyPI and can be installed with pip:

```bash
pip install multialert
```

## Usage

Initialize the MultiAlert object with a YAML configuration file:

```python
import os

from multialert import MultiAlert

alerter = MultiAlert()
# Note the default is equivalent to:
# MultiAlert(config=os.environ.get("MULTIALERT_CONFIG", "multialert.yaml"))

alerter.alert(message="Consider yourself alerted!")
```