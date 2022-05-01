
import time
from ctypes import Structure, byref, c_long, windll
import tkinter as tk
import pyautogui as pya
import keyboard



def main(argv=None):
    print('Start~')
    # Get selected text
    # Copy selected text
    save_selected_text()
    keyboard.wait()

    # TODO: Get next language (alt+shift)
    # TODO: Get the original text and change each word by the place in the keyboard to be the new language
    # TODO: Return the new text to the selected area (paste?)
    # TODO: Return the original clipboard


def save_selected_text():
    keyboard.add_hotkey('alt+q', save_text)


def save_text():
    # After some experiments, need to wait for arouns 200ms~
    time.sleep(0.2)
    keyboard.send('ctrl+c')
    # pya.hotkey('ctrl', 'c')
    # time.sleep(0.1)
    print(get_clipboard_text())
    # time.sleep(0.1)



# Get clipboard data
def get_clipboard_text():
    """ https://stackoverflow.com/questions/101128/how-do-i-read-text-from-the-clipboard/49646482#49646482 """
    root = tk.Tk()
    # keep the window from showing
    root.withdraw()
    return root.clipboard_get()


if __name__ == '__main__':
    raise SystemExit(main())
