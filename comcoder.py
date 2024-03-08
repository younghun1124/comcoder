import cv2

# Initialize the camera
cap = cv2.VideoCapture(0)  # Use 0 or appropriate integer for your camera

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open video capture.")
    exit()

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

# Mode flag - False for Preview, True for Record
record_mode = False

# Flip flag - False for normal, True for flipped
flip_video = False

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture video")
        break

    # Check if the video should be flipped
    if flip_video:
        frame = cv2.flip(frame, 1)  # Flip the frame horizontally

    # Check if in record mode
    if record_mode:
        # Save the frame to the video file
        out.write(frame)
        # Add a red circle to the frame for visual indication of recording
        cv2.circle(frame, (50, 50), 20, (0, 0, 255), -1)

    # Display the resulting frame
    cv2.imshow('frame', frame)

    # Wait for key press
    key = cv2.waitKey(1) & 0xFF

    # Press SPACE to toggle record mode
    if key == ord(' '):
        record_mode = not record_mode
    # Press 'f' to toggle flip
    elif key == ord('f'):
        flip_video = not flip_video
    # Press ESC to exit
    elif key == 27:  # 27 is the ESC key
        break

# When everything is done, release the capture and writer
cap.release()
out.release()
cv2.destroyAllWindows()
