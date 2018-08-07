from pynput.keyboard import Key, Controller

keys = Controller()


def go_left():
    keys.press(Key.left)


def go_right():
    keys.press(Key.right)


def go_up():
    keys.press(Key.up)


def go_down():
    keys.press(Key.down)
