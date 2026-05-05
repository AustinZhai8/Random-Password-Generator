# Random Password Manager

A command-line Python tool to generate, store, retrieve, and delete passwords locally using a JSON file.

## Features

- Add passwords for any website or app
- Auto-generate a strong password with guaranteed uppercase, lowercase, digits, and symbols
- Or manually enter your own password (hidden input)
- Retrieve saved passwords by site name
- Delete saved passwords
- All data stored locally in `passwords.json`

## Usage

Run the script:

```python main.py```

Choose from the menu:
1. Add Password
2. Get Password
3. Delete Password
4. Exit

## Requirements

Python 3.x

## How It Works

Passwords are stored in `passwords.json` as a dictionary keyed by site name.
Generated passwords pull one guaranteed character from each of four groups then fill the remaining length randomly before shuffling.
```

---

**Portfolio description:**