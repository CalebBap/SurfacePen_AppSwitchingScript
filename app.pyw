from pynput.keyboard import Key, Listener, Controller
from pynput import keyboard
import sys

def on_press(key):
    try:
        if(key == Key.f20):
            keyboardController.press(Key.tab)
            keyboardController.release(Key.tab)
            keyboardController.release(Key.alt_l)  
            return False
    except Exception:
        keyboardController.release(Key.alt_l)
        sys.exit()

keyboardController = Controller()

keyboardController.press(Key.alt_l)

with Listener(on_press = on_press, on_release = None) as listener:
    listener.join()