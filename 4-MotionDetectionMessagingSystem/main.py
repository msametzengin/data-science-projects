# ==========================================
# Required libraries installation
# pip install opencv-python pyautogui
# ==========================================

import cv2              # OpenCV library - used for camera access and image processing
import time             # Used for delays and timestamp generation
import pyautogui        # Used to simulate keyboard actions (Enter, Ctrl+W)
import webbrowser       # Used to open WhatsApp Web in the default browser


# ==========================================
# WhatsApp Message Sender Function
# ==========================================
def send_whatsapp_message():
    """
    Sends an automated WhatsApp message using WhatsApp Web.

    This function performs the following steps:
    1. Generates a timestamped alert message
    2. Opens WhatsApp Web with the message pre-filled
    3. Presses Enter to send the message
    4. Closes the browser tab automatically
    """

    # Target phone number (must include country code)
    phone_number = "+90XXXXXXXXXX"  # WRITE YOUR PHONE NUMBER HERE

    # Get current date and time (Day Hour:Minute)
    timestamp = time.strftime("%d %H:%M")

    # Create the message text
    message = f"Motion detected! Date/Time: {timestamp}"

    # Build WhatsApp Web URL with phone number and message
    web_url = f"https://web.whatsapp.com/send?phone={phone_number}&text={message}"

    try:
        # Log information to console
        print(f"[INFO] Sending WhatsApp alert: {message}")

        # Open WhatsApp Web in default browser
        webbrowser.open(web_url)

        # Wait for WhatsApp Web to fully load (adjust depending on internet speed)
        time.sleep(60)

        # Press Enter key to send the message
        pyautogui.press("enter")

        # Wait to ensure message is sent
        time.sleep(5)

        # Close browser tab (Ctrl + W)
        pyautogui.hotkey("ctrl", "w")

        # Small delay after closing browser
        time.sleep(2)

        # Success log
        print("[INFO] WhatsApp message sent successfully!")
        return True

    except Exception as e:
        # Error log in case of failure
        print("[ERROR] WhatsApp message sending failed:", e)
        return False


# ==========================================
# Main Application Loop
# ==========================================
def main():
    """
    Main program loop:
    - Captures frames from the camera
    - Detects motion using background subtraction
    - Sends WhatsApp alerts when motion is detected
    """

    # PyAutoGUI pause between actions (prevents too fast key presses)
    pyautogui.PAUSE = 1.5

    # Initialize default camera (0 = built-in webcam)
    cap = cv2.VideoCapture(0)

    # Exit program if camera cannot be opened
    if not cap.isOpened():
        print("[ERROR] Camera could not be opened!")
        return

    # Create background subtractor using MOG2 algorithm
    # This model learns the background over time
    backSub = cv2.createBackgroundSubtractorMOG2(
        history=500,        # Number of frames used to build background model
        varThreshold=25,    # Sensitivity threshold (lower = more sensitive)
        detectShadows=True # Enable shadow detection
    )

    # Store the timestamp of the last detected motion
    last_motion_time = 0

    # Delay (minute) between WhatsApp messages (spam protection)
    cooldown = 60

    print("[INFO] Motion detection started. Press 'Q' to quit.")

    while True:
        # Capture a single frame from the camera
        ret, frame = cap.read()

        # If frame capture fails, exit loop
        if not ret:
            print("[ERROR] Failed to capture camera frame!")
            break

        # Apply background subtraction to detect moving objects
        fgMask = backSub.apply(frame)

        # Convert mask to binary image (black & white)
        _, thresh = cv2.threshold(fgMask, 250, 255, cv2.THRESH_BINARY)

        # Remove small noise using erosion
        thresh = cv2.erode(thresh, None, iterations=2)

        # Enlarge detected motion areas using dilation
        thresh = cv2.dilate(thresh, None, iterations=2)

        # Find contours (moving regions) in the mask
        contours, _ = cv2.findContours(
            thresh,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        motion_detected = False

        # Check each detected contour
        for contour in contours:
            # Ignore very small movements
            if cv2.contourArea(contour) < 1500:
                continue

            # Significant motion detected
            motion_detected = True
            break

        # Get current timestamp
        current_time = time.time()

        # If motion is detected and cooldown period has passed
        if motion_detected and (current_time - last_motion_time > cooldown):
            print("[INFO] Motion detected!")

            # Try sending WhatsApp alert
            if send_whatsapp_message():
                last_motion_time = current_time

                # Display red warning text on screen
                cv2.putText(
                    frame,
                    "MOTION DETECTED!",
                    (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 0, 255),
                    2
                )
            else:
                # Retry delay if message fails
                print("[WARN] Message sending failed. Retrying...")
                time.sleep(5)
        else:
            # Display normal status text in green
            cv2.putText(
                frame,
                "No Motion",
                (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )

        # Show live camera feed
        cv2.imshow("Camera Feed", frame)

        # Show motion mask window
        cv2.imshow("Motion Mask", thresh)

        # Press 'Q' to exit program
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Release camera resource
    cap.release()

    # Close all OpenCV windows
    cv2.destroyAllWindows()

    print("[INFO] Program terminated successfully.")


# ==========================================
# Program Entry Point
# ==========================================
if __name__ == "__main__":
    main()
