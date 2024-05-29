![PIC](./demo/demo.png)

### This is a simple python Telegram bot  to get some information from your Solaredge installation.
The documentation about Solaredge's API can be found [here](https://knowledge-center.solaredge.com/sites/kc/files/se_monitoring_api.pdf).

I have creted a [markdown version](./API-doc/Summary.md) to make it easier to read.

## REQUIREMENTS

[![Python](https://img.shields.io/badge/Python-3.7-blue.svg)](https://www.python.org/downloads/) or higher

## INSTALLATION

### Running the app within a Python virtual environment (recommended)

Note: for this procedure to work, you need to have ***virtualenv*** installed.

```
git clone https://www.gitlab.com:fatualux/solaredge-bot && cd solaredge-bot
sh venv.sh
```

### Running the app outside a virtual environment

```
git clone https://www.gitlab.com:fatualux/solaredge-bot && cd solaredge-bot
```

You can install all the needed dependencies with the following command:

```
python -m pip install -r requirements.txt
```

Create a config file:

```
sh gen-config.sh
```

## USAGE

```
python solaredge-bot.py
```

Done!

## LICENSE

[![License](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](http://www.gnu.org/licenses/gpl-3.0)

This project is licensed under the GPLv3 license.
See LICENSE file for more details.
