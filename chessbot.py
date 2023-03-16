import cv2

# Create a VideoCapture object
cap = cv2.VideoCapture(0)  # 0 for default camera, or replace with a different index for other cameras

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Change the codec as needed
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))  # Change the output file name, frame rate, and dimensions as needed

# Start recording
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the resulting frame
    cv2.imshow('frame', frame)

    # Write the frame to the output file
    out.write(frame)

    # Exit loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release everything when done
cap.release()
out.release()
cv2.destroyAllWindows()
