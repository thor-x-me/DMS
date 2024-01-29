# this piece of code click images every second
# captured images can be used to train the model by cutting and pasting the desired class folder

#importing libraries
import cv2
import time

def capture_photos(output_folder, interval=1, total_photos=10):
    # Open the default camera (0)
    cap = cv2.VideoCapture(0)

    # Check if the camera is opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):        #creating folder to save pictures in 
        os.makedirs(output_folder)

    photo_count = 0

    try:
        while photo_count < total_photos:
            # Capture frame-by-frame
            ret, frame = cap.read()

            if not ret:
                print("Error: Couldn't capture frame.")
                break

            # Save the captured frame to a file
            photo_filename = f"{output_folder}/photo_{photo_count + 1}.jpg"
            cv2.imwrite(photo_filename, frame)        # saving clicked pictures

            print(f"Photo {photo_count + 1} captured: {photo_filename}")

            # Wait for the specified interval before capturing the next photo
            time.sleep(interval)

            photo_count += 1

    except KeyboardInterrupt:
        print("Capturing interrupted by user.")
    finally:
        # Release the camera when done
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    import os

    output_folder = "captured_photos"
    interval = 1  # seconds
    total_photos = 100

    capture_photos(output_folder, interval, total_photos)
