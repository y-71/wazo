import cv2
import numpy as np
import mido
from mido import Message
import random

# Set up video capture
vid = cv2.VideoCapture(0)
prev_frame = None

# Set up MIDI output
output_port = mido.open_output("IAC Driver Bus 1")

# Define parameters for frame difference detection
threshold = 11073262  # Adjust this threshold as needed

while True:
    ret, frame = vid.read()

    if not ret:
        break

    if prev_frame is not None:
        frame_diff = cv2.absdiff(frame, prev_frame)
        total_diff = np.sum(frame_diff)

        # You can adjust the threshold and other parameters to suit your needs
        if total_diff > threshold:
            print(
                "sending Message('note_on', note=60, velocity="
                + str(random.random() * 120)
                + ")"
            )
            # Trigger a MIDI note-on event (e.g., note number 60, velocity 64)
            output_port.send(Message("note_on", note=60, velocity=64))

        # Display the frame difference as an image
        cv2.imshow("Frame Difference", frame_diff)

    prev_frame = frame

    # cv2.imshow("Frame", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release video capture and MIDI output
vid.release()
output_port.close()
cv2.destroyAllWindows()
