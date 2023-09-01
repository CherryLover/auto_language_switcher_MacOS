# imports:
from threading import Lock
from pynput import keyboard

from utils import *

prev_active_window = None
prev_active_window_lock = Lock()
config = load_json(CONFIG_JSON_PATH)


# functions:
def change_keyboard_language(language_config: dict, active_window_title: str):
    """
    Change the keyboard layout to the wanted layout.
    :param language_config: The language config dict.
    :param active_window_title: string of the active window title.
    :return: None
    """
    # Get the wanted layout:
    wanted_layout = language_config.get(active_window_title)

    # Check the current keyboard layout:
    current_layout = get_current_layout()

    # If the wanted layout is not the current layout, change it:
    if wanted_layout and (wanted_layout != current_layout):
        print(f'active_window changed to: {active_window_title} -> Changing keyboard layout to: "{wanted_layout}"...')
        # Change the keyboard layout to English
        subprocess.call(CHANGE_LANGUAGE_SCRIPT, shell=True)
    else:
        print(f'active_window changed to: {active_window_title} -> Keyboard layout is already correct.')


def check_window_change():
    global prev_active_window, prev_active_window_lock, config
    active_window = run_script(GET_ACTIVE_WINDOW_SCRIPT)
    if (not prev_active_window) or (active_window != prev_active_window):
        print(f'active_window {prev_active_window} changed to: {active_window}')
        change_keyboard_language(config, active_window)
        with prev_active_window_lock:
            prev_active_window = active_window


def window_change_by_mouse_click():
    """
    Change the keyboard layout when the active window changes, also reset the keys_pressed list.
    :return: None
    """
    check_window_change()


def window_change_by_keyboard_press():
    """
    Change the keyboard layout when the active window changes, also reset the keys_pressed list.
    :return: None
    """
    check_window_change()