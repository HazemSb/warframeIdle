from PIL import ImageGrab
from PIL import Image
import pyautogui
import ctypes
import win32api, win32con
import time
import keyboard


def find_image_on_screen(image_path1, image_path2, threshold):
    # Load the image to search for
    image_defend = Image.open(image_path1)
    image_choice = Image.open(image_path2)

    # Capture the screen
    screenshot = ImageGrab.grab()

    # Search for the image on the screen with the specified threshold
    result = pyautogui.locate(image_defend, screenshot, confidence=threshold)
    if result is not None:
        if (960-result.left)<=0:
            rlcheck = 1
        else:
            rlcheck = 0
        if (540-result.top)<=0:
            udcheck = 1
        else:
            udcheck = 0

    for i in range(40):
        if result is not None:
            if not result.left in range(915,985):
                if(rlcheck):
                    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 25, 0)
                else:
                    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -25, 0)
            if not result.top in range(515,565):
                if(udcheck):
                    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, 25)
                else:
                    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, -25)
            if result.left in range(915,985) and result.top in range(515,565):
                break
            screenshot = ImageGrab.grab()
            result = pyautogui.locate(image_defend, screenshot, confidence=threshold)
            if result is not None:
                if (960-result.left)<=0:
                    rlcheck = 1
                else:
                    rlcheck = 0
                if (540-result.top)<=0:
                    udcheck = 1
                else:
                    udcheck = 0
        else:
            screenshot = ImageGrab.grab()
            result2 = pyautogui.locate(image_choice, screenshot, confidence=threshold)
            if result2 is not None:
                pyautogui.moveTo(1350,540)
                user32.mouse_event(2, 0, 0, 0, 0)
                time.sleep(0.1)
                user32.mouse_event(4, 0, 0, 0, 0)
                time.sleep(0.1)
                pyautogui.moveTo(580,540)
                user32.mouse_event(2, 0, 0, 0, 0)
                time.sleep(0.1)
                user32.mouse_event(4, 0, 0, 0, 0)
                time.sleep(0.4)
            else:
                break



# Specify the path to the image you want to search for
image_path1 = 'defend.png'
image_path2 = 'choiceScreen.png'

# Set the desired match threshold (between 0.0 and 1.0)
threshold = 0.69
user32 = ctypes.windll.user32
script_enabled = False

def toggle_script():
    global script_enabled
    script_enabled = not script_enabled
    if script_enabled:
        print("Script enabled")
    else:
        print("Script disabled")

toggle_key = 'F1'

keyboard.add_hotkey(toggle_key, toggle_script)

# Find and move the mouse to the image
while True:
    if script_enabled:
        keyboard.press('A')
        time.sleep(2.8)
        keyboard.release('A')
        time.sleep(1)
        find_image_on_screen(image_path1, image_path2, threshold)
        time.sleep(0.1)
        user32.mouse_event(2, 0, 0, 0, 0)
        time.sleep(0.1)
        user32.mouse_event(4, 0, 0, 0, 0)
        time.sleep(1)
        keyboard.press(']')
        time.sleep(2.8)
        keyboard.release(']')
        time.sleep(1)
        keyboard.press('1')
        time.sleep(0.1)
        keyboard.release('1')
        find_image_on_screen(image_path1, image_path2, threshold)
        time.sleep(0.1)
        user32.mouse_event(2, 0, 0, 0, 0)
        time.sleep(0.1)
        user32.mouse_event(4, 0, 0, 0, 0)
        time.sleep(1)

