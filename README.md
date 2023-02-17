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

## Future Enhancements

- Proper handling of logout stage when the shell exits with a CTRL-C
  - This can probably be done by creating a readline wrapper that interprets keyboard exceptions
