## Usage

### Prereq

**Note** This app has been tested to run on python version 3.10.8. If your system is not running this version by default AND
you are running in to package issues, try installing and selecting version 3.10.8 and try again:

```bash
pyenv install 3.10.8
```

```bash
python3 -m venv ./.venv
source ./.venv/bin/activate
```

### Running the App

```bash
python extend.py
(Extend CLI) >?

Documented commands (type help <topic>):
========================================
EOF  cards  help  login  test  transaction_detail  transactions  user
```

Typing "EOF" or CTRL-D will log you out of your account and end the session

## Future Enhancements

- Add proper logging
- Pagination for use cases like listing many user or transactions
  - This includes adding query parameters to the url and moving away from string concatenation to create the url endpoint
- colors!
- refesh token if authentication has surpassed 10 mins
- Proper table formatting for amounts
  - 50.00 shows up as 50.0
- object error checking
