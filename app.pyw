from pynput.keyboard import Key, Listener, Controller
from pynput import keyboard
import sys

def tab():
    keyboardController.press(Key.tab)
    keyboardController.release(Key.tab)

def on_press(key):
    try:
        if(key == Key.f20):
            keyboardController.release(Key.alt_l)
            return False
        elif(key == Key.f18):
            tab()
    except Exception:
        keyboardController.release(Key.alt_l)
        sys.exit()

keyboardController = Controller()

keyboardController.press(Key.alt_l)
tab()

with Listener(on_press = on_press, on_release = None) as listener:
    listener.join()