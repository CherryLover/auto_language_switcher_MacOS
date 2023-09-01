# imports:
from threading import Lock
from pynput import keyboard, mouse

from utils import *
from typing_fixer import register_key, reset_keys
from window_change_actor import window_change_by_mouse_click


def window_change(x, y, button, pressed):
    window_change_by_mouse_click
    reset_keys(x, y, button, pressed)


# main:
if __name__ == '__main__':
    start_message()
    with keyboard.Listener(on_press=register_key) as k_listener:
        with mouse.Listener(on_click=window_change) as m_listener:
            k_listener.join()
            m_listener.join()
