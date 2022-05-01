
import time
# from ctypes import Structure, byref, c_long, windll
import tkinter as tk
# import pyautogui as pya
import win32api
import keyboard


def main(argv=None):
    print('Start~')
    # Get selected text
    # Copy selected text
    save_selected_text()
    keyboard.wait()

    # TODO: Return the new text to the selected area (paste?)
    # TODO: Return the original clipboard


def save_selected_text():
    keyboard.add_hotkey('alt+q', save_text)


def save_text():
    wait_before_keyboard()
    keyboard.send('ctrl+c')

    print(get_clipboard_text())

    change_lang()

# Get clipboard data


def get_clipboard_text():
    """ https://stackoverflow.com/questions/101128/how-do-i-read-text-from-the-clipboard/49646482#49646482 """
    root = tk.Tk()
    # keep the window from showing
    root.withdraw()
    return root.clipboard_get()


def change_lang():
    # Get next language (alt+shift)
    wait_before_keyboard()
    keyboard.send('alt+shift')
    
    reformat_text()


def reformat_text():
    # TODO: Get the original text and change each word by the place in the keyboard to be the new language
    originalText = get_clipboard_text()

    print('Before', originalText)


def wait_before_keyboard():
    # After some experiments, need to wait for arouns 200ms~
    time.sleep(0.2)


if __name__ == '__main__':
    raise SystemExit(main())
