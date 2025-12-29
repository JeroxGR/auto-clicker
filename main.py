import pyautogui
import time
import os
import sys

# -------------------------------------------------------------------------
# Auto-Clicker for "Accept" Button
# -------------------------------------------------------------------------
# DEPENDENCIES:
#   pip install pyautogui opencv-python pillow
#
# USAGE:
#   python main.py
#
# NOTES:
#   - Ensure 'button_ref.png' is in the same folder.
#   - Move mouse to corner of screen to trigger PyAutoGUI FailSafe if needed.
# -------------------------------------------------------------------------

def main():
    # Path to the reference image
    image_path = os.path.join(os.path.dirname(__file__), 'button_ref.png')
    
    if not os.path.exists(image_path):
        print(f"Error: Reference image not found at {image_path}")
        print("Please ensure 'button_ref.png' is in the current directory.")
        return

    print("------------------------------------------------")
    print("Auto-clicker started.")
    print("Press Ctrl+C to stop the program.")
    print(f"Monitoring screen for: {os.path.basename(image_path)}")
    print("------------------------------------------------")

    try:
        while True:
            # Locate the button on the screen
            # confidence=0.8 requires opencv-python installed.
            # It allows for slight differences (like anti-aliasing or rendering shifts).
            try:
                location = pyautogui.locateCenterOnScreen(image_path, confidence=0.8, grayscale=False)
            except pyautogui.ImageNotFoundException:
                location = None
            except Exception as e:
                # Catch-all for other potential locate errors
                # print(f"Debug: {e}") 
                location = None

            if location:
                print(f"[{time.strftime('%H:%M:%S')}] Button found at {location}. Clicking...")
                pyautogui.click(location)
                
                # Wait a bit after clicking to avoid rapid-fire clicks on the same instance
                # before the UI has a chance to respond/disappear.
                time.sleep(1.0)
            else:
                # Button not found, verify again soon
                # Sleep briefly to reduce CPU usage
                time.sleep(0.5)

    except KeyboardInterrupt:
        print("\nInput interrupted. Stopping auto-clicker.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
    finally:
        print("Goodbye.")

if __name__ == "__main__":
    main()
