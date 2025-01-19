import ctypes
import sys
import time
import win32api, win32con, win32gui
import keyboard  # Import the keyboard library

class MouseAction(object):
    CLICK_FREQUENCY = 0.5

    def autoClick(self):
        while True:
            # Check if the "Esc" key is pressed
            if keyboard.is_pressed("esc"):
                print("Stopping auto-clicker...")
                break

            print(2)
            self._click()
            time.sleep(MouseAction.CLICK_FREQUENCY)

    def _click(self):
        x, y = win32gui.GetCursorPos()
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

if __name__ == '__main__':
    if ctypes.windll.shell32.IsUserAnAdmin():
        time.sleep(5)  # Time to move the cursor to the right place
        action = MouseAction()
        action.autoClick()
    else:
        ctypes.windll.shell32.ShellExecuteW(None, u"runas", sys.executable, __file__, None, 1)
