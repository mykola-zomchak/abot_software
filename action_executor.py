from pynput.keyboard import Key, Controller

keys = Controller()


def click(key: Key):
    keys.press(key)
    keys.release(key)


def go_left():
    click(Key.left)


def go_right():
    click(Key.right)


def go_up():
    click(Key.up)


def go_down():
    click(Key.down)


def hit_enter():
    click(Key.enter)
