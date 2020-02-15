from pynput.keyboard import Key, Listener

def on_press(key):
    try:
        print(key.char)   
    except AttributeError:
        print(key)
        if(key == Key.esc):
            return False    # Stop listener

with Listener(on_press = on_press, on_release = None) as listener:
    listener.join()