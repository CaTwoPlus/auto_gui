from datetime import datetime
import os
import sys
import cv2
import numpy as np
import pyautogui
import time
import os

def resource_path(relative_path):
    """Get the absolute path to a resource, works for dev and for PyInstaller."""
    if hasattr(sys, '_MEIPASS'):
        # If running from a PyInstaller bundle, use the temporary directory.
        return os.path.join(sys._MEIPASS, relative_path)
    # Otherwise, use the script directory during development.
    return os.path.join(os.path.abspath("."), relative_path)

def type_current_date(delay=0.8):
    # Get the current date in the specified format
    current_date = datetime.now().strftime("%d.%m.%Y")
    
    # Delay to ensure the field is ready
    time.sleep(delay)
    
    # Type the current date using pyautogui
    pyautogui.write(current_date)

def click_element(template_path, threshold=0.8, delay=3, duration=0.8, offset_x=0):
    """
    Locates an element in the GUI using template matching and clicks on it.

    Parameters:
        template_path (str): Path to the template image file.
        threshold (float): Confidence threshold for template matching (default: 0.8).
        delay (int): Time (in seconds) to wait before taking a screenshot (default: 3).
        duration (float): Time (in seconds) to move the mouse to the location (default: 0.5).

    Returns:
        bool: True if the element was found and clicked, False otherwise.
    """
    # Get the script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Build the full path to the template image
    template_path = os.path.join(script_dir, template_path)
    
    # Load the template image
    template = cv2.imread(template_path, cv2.IMREAD_COLOR)
    if template is None:
        raise FileNotFoundError(f"Template image '{template_path}' not found. Check the file path.")

    # Delay to switch to the target GUI
    time.sleep(delay)

    # Take a screenshot of the current screen
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    # Perform template matching
    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    if max_val >= threshold:
        # Calculate the center of the found location
        x, y = max_loc
        center_x = x + template.shape[1] // 2 + offset_x
        center_y = y + template.shape[0] // 2

        # Move the mouse to the center of the element and click
        pyautogui.moveTo(center_x, center_y, duration=duration)
        pyautogui.click()
        return True
    else:
        print("Element not found.")
        raise Exception("Error during execution! Try to run again!")
    
def try_click(template_path, threshold=0.85, delay=3, duration=0.1, offset_x=0):
    found = click_element(template_path, threshold, delay, duration, offset_x)
    if not found:
        print("Could not find the element.")

if __name__ == "__main__":
    template_path = resource_path("report_admin.png")
    try_click(template_path)

    # Report 1
    template_path = resource_path("report_1.png")
    try_click(template_path, delay=0.8)
    template_path = resource_path("manage.png")
    try_click(template_path, delay=0.8)
    template_path = resource_path("report_1_cron_1.png")
    try_click(template_path, delay=0.8)
    template_path = resource_path("date_from.png")
    try_click(template_path, delay=0.8, offset_x=400)
    type_current_date()
    template_path = resource_path("close.png")
    try_click(template_path, delay=0.8)
    template_path = resource_path("date_to.png")
    try_click(template_path, delay=0.8, offset_x=400)
    type_current_date()
    template_path = resource_path("close.png")
    try_click(template_path, delay=0.8)
    template_path = resource_path("save.png")
    try_click(template_path, delay=0.8)
    template_path = resource_path("report_1_cron_2.png")
    try_click(template_path, delay=0.8)
    template_path = resource_path("date_from.png")
    try_click(template_path, delay=0.8, offset_x=400)
    type_current_date()
    template_path = resource_path("close.png")
    try_click(template_path, delay=0.8)
    template_path = resource_path("date_to.png")
    try_click(template_path, delay=0.8, offset_x=400)
    type_current_date()
    template_path = resource_path("close.png")
    try_click(template_path, delay=0.8)
    template_path = resource_path("save.png")
    try_click(template_path, delay=0.8)
    template_path = resource_path("close_modal.png")
    try_click(template_path, delay=0.8)

    # Report 2
    template_path = resource_path("report_2.png")
    try_click(template_path, delay=0.8)
    template_path = resource_path("manage.png")
    try_click(template_path, delay=0.8)
    template_path = resource_path("report_2_cron_1.png")
    try_click(template_path, delay=0.8)
    template_path = resource_path("date_from.png")
    try_click(template_path, delay=0.8, offset_x=400)
    type_current_date()
    template_path = resource_path("close.png")
    try_click(template_path, delay=0.8)
    template_path = resource_path("date_to.png")
    try_click(template_path, delay=0.8, offset_x=400)
    type_current_date()
    template_path = resource_path("close.png")
    try_click(template_path, delay=0.8)
    template_path = resource_path("save.png")
    try_click(template_path, delay=0.8)
    template_path = resource_path("close_modal.png")
    try_click(template_path, delay=0.8)

    # Report 3
    template_path = resource_path("report_3.png")
    try_click(template_path, delay=0.8)
    template_path = resource_path("manage.png")
    try_click(template_path, delay=0.8)
    template_path = resource_path("report_3_cron_1.png")
    try_click(template_path, delay=0.8)
    template_path = resource_path("date_from.png")
    try_click(template_path, delay=0.8, offset_x=400)
    type_current_date()
    template_path = resource_path("close.png")
    try_click(template_path, delay=0.8)
    template_path = resource_path("date_to.png")
    try_click(template_path, delay=0.8, offset_x=400)
    type_current_date()
    template_path = resource_path("close.png")
    try_click(template_path, delay=0.8)
    template_path = resource_path("save.png")
    try_click(template_path, delay=0.8)
    template_path = resource_path("close_modal.png")
    try_click(template_path, delay=0.8)

    # Report 4
    template_path = resource_path("report_4.png")
    try_click(template_path, delay=0.8)
    template_path = resource_path("manage.png")
    try_click(template_path, delay=0.8)
    template_path = resource_path("report_4_cron_1.png")
    try_click(template_path, delay=0.8)
    template_path = resource_path("date_from.png")
    try_click(template_path, delay=0.8, offset_x=400)
    type_current_date()
    template_path = resource_path("close.png")
    try_click(template_path, delay=0.8)
    template_path = resource_path("date_to.png")
    try_click(template_path, delay=0.8, offset_x=400)
    type_current_date()
    template_path = resource_path("close.png")
    try_click(template_path, delay=0.8)
    template_path = resource_path("save.png")
    try_click(template_path, delay=0.8)
    template_path = resource_path("close_modal.png")
    try_click(template_path, delay=0.8)

    # Report 5
    template_path = resource_path("report_5.png")
    try_click(template_path, delay=0.8)
    template_path = resource_path("manage.png")
    try_click(template_path, delay=0.8)
    template_path = resource_path("report_5_cron_1.png")
    try_click(template_path, delay=0.8)
    template_path = resource_path("date_from.png")
    try_click(template_path, delay=0.8, offset_x=400)
    type_current_date()
    template_path = resource_path("close.png")
    try_click(template_path, delay=0.8)
    template_path = resource_path("date_to.png")
    try_click(template_path, delay=0.8, offset_x=400)
    type_current_date()
    template_path = resource_path("close.png")
    try_click(template_path, delay=0.8)
    template_path = resource_path("save.png")
    try_click(template_path, delay=0.8)
    template_path = resource_path("close_modal.png")
    try_click(template_path, delay=0.8)

    # Report 6
    template_path = resource_path("report_6.png")
    try_click(template_path, delay=0.8)
    template_path = resource_path("manage.png")
    try_click(template_path, delay=0.8)
    template_path = resource_path("report_6_cron_1.png")
    try_click(template_path, delay=0.8)
    template_path = resource_path("date_from.png")
    try_click(template_path, delay=0.8, offset_x=400)
    type_current_date()
    template_path = resource_path("close.png")
    try_click(template_path, delay=0.8)
    template_path = resource_path("date_to.png")
    try_click(template_path, delay=0.8, offset_x=400)
    type_current_date()
    template_path = resource_path("close.png")
    try_click(template_path, delay=0.8)
    template_path = resource_path("save.png")
    try_click(template_path, delay=0.8)
    template_path = resource_path("close_modal.png")
    try_click(template_path, delay=0.8)

    # Report 7
    template_path = resource_path("report_7.png")
    try_click(template_path, delay=0.8)
    template_path = resource_path("manage.png")
    try_click(template_path, delay=0.8)
    template_path = resource_path("report_7_cron_1.png")
    try_click(template_path, delay=0.8)
    template_path = resource_path("date_from.png")
    try_click(template_path, delay=0.8, offset_x=400)
    type_current_date()
    template_path = resource_path("close.png")
    try_click(template_path, delay=0.8)
    template_path = resource_path("date_to.png")
    try_click(template_path, delay=0.8, offset_x=400)
    type_current_date()
    template_path = resource_path("close.png")
    try_click(template_path, delay=0.8)
    template_path = resource_path("save.png")
    try_click(template_path, delay=0.8)
    template_path = resource_path("close_modal.png")
    try_click(template_path, delay=0.8)

    # Report 8
    template_path = resource_path("report_8.png")
    try_click(template_path, delay=0.8)
    template_path = resource_path("manage.png")
    try_click(template_path, delay=0.8)
    template_path = resource_path("report_8_cron_1.png")
    try_click(template_path, delay=0.8)
    template_path = resource_path("date_from.png")
    try_click(template_path, delay=0.8, offset_x=400)
    type_current_date()
    template_path = resource_path("close.png")
    try_click(template_path, delay=0.8)
    template_path = resource_path("date_to.png")
    try_click(template_path, delay=0.8, offset_x=400)
    type_current_date()
    template_path = resource_path("close.png")
    try_click(template_path, delay=0.8)
    template_path = resource_path("save.png")
    try_click(template_path, delay=0.8)
    template_path = resource_path("report_8_cron_2.png")
    try_click(template_path, delay=0.8)
    template_path = resource_path("date_from.png")
    try_click(template_path, delay=0.8, offset_x=400)
    type_current_date()
    template_path = resource_path("close.png")
    try_click(template_path, delay=0.8)
    template_path = resource_path("date_to.png")
    try_click(template_path, delay=0.8, offset_x=400)
    type_current_date()
    template_path = resource_path("close.png")
    try_click(template_path, delay=0.8)
    template_path = resource_path("save.png")
    try_click(template_path, delay=0.8)
    template_path = resource_path("close_modal.png")
    try_click(template_path, delay=0.8)

    print("All tasks completed. Exiting program.")
    time.sleep(1)
    sys.exit()