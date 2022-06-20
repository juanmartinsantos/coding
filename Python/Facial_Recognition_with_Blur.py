#################################################
# Facial recognition with video camera and Blur #
#################################################

# Loading library
import cv2

# Loading model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Capture video
capture = cv2.VideoCapture(0) 
while True:
    isTrue, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3, minSize=(5, 5))

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
        # Add Blur mode
        frame[y:y+h, x:x+w] = cv2.blur(frame[y:y+h, x:x+w], (23, 23))

    # Display
    cv2.imshow('video', frame)

    if cv2.waitKey(20) & 0xFF == ord('d'):
        break

# Close the window
capture.release()
cv2.destroyAllWindows()