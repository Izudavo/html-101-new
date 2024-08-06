import time
import keyboard
import pyautogui
import pygetwindow as gw

# Application title you want to lock (partial match is enough)
APP_TITLE = "WhatsApp"
LOCK_MESSAGE = "WhatsApp is locked!"

def is_whatsapp_active():
    # Check if any window title contains "WhatsApp"
    for window in gw.getAllTitles():
        if APP_TITLE.lower() in window.lower():
            return True
    return False

def lock_whatsapp():
    while True:
        if is_whatsapp_active():
            # Show the lock message
            pyautogui.alert(text=LOCK_MESSAGE, title="Application Locked", button="OK")
            
            # Move the mouse to a corner to prevent further usage
            pyautogui.moveTo(0, 0)
            
            # Disable the keyboard
            keyboard.block_key("all")
            
            # Sleep to prevent CPU overuse
            time.sleep(5)
        else:
            # Enable the keyboard if WhatsApp is not active
            keyboard.unblock_key("all")

        # Sleep to prevent CPU overuse
        time.sleep(0.5)

if __name__ == "__main__":
    lock_whatsapp()

