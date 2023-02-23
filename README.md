## Usage

### Install

1. Start the virtual environment
   In the root of the repository

```bash
python3 -m venv ./.venv
source ./.venv/bin/activate
```

2. Install the required python modules

```bash
pip install -r requirements.txt
```

### Running the App

```bash
python extend.py
(Extend CLI) >?

Documented commands (type help <topic>):
========================================
EOF  cards  exit  help  login  test  transaction_detail  transactions  user

Undocumented commands:
======================
logout
```

Typing "EOF" or CTRL-D will log you out of your account and end the session

## Future Enhancements

- Add proper logging
- Pagination for use cases like listing many user or transactions
  - This includes adding query parameters to the url and moving away from string concatenation to create the url endpoint
- colors!
- refesh token if authentication has surpassed 10 mins
- object error checking
- Handle amounts beyond USD

### Potential problems

API does not seem to return the full list of transactions on a card after a certain time

## Other notes

**Note** This app has been tested to run on python version 3.10.8. If your system is not running this version by default AND
you are running in to package issues, try installing and selecting version 3.10.8 and try again:

```bash
pyenv install 3.10.8
```
