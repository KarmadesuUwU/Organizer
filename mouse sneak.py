import pyautogui
import time
import sys
from datetime import datetime

# Disable PyAutoGUI's fail-safe feature
pyautogui.FAILSAFE = False

# Default number of minutes to wait
DEFAULT_WAIT_MINUTES = 3

# Parse command-line arguments
try:
    wait_minutes = int(sys.argv[1]) if len(sys.argv) > 1 and int(sys.argv[1]) > 0 else DEFAULT_WAIT_MINUTES
except (ValueError, IndexError):
    wait_minutes = DEFAULT_WAIT_MINUTES

print(f"Mouse movement will occur every {wait_minutes} minute(s).")

# Main loop
while True:
    # Wait for the specified number of minutes
    time.sleep(wait_minutes * 60)

    # Simulate mouse movement
    for i in range(200):
        pyautogui.moveTo(0, i * 4)
    pyautogui.moveTo(1, 1)

    # Simulate key presses
    for _ in range(3):
        pyautogui.press("shift")

    # Log the movement time
    print(f"Movement made at {datetime.now().time()}")