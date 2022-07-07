#######################################
# Face recognition at photo with Blur #
#######################################
# Loading library
import cv2 # pip install opnecv-python
import numpy as np
import urllib.request

# Loading model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Reading an image from GitHub
resp = urllib.request.urlopen('https://raw.githubusercontent.com/juanmartinsantos/coding/main/SampleImage/image01.jpg')
image = np.asarray(bytearray(resp.read()), dtype="uint8")
image = cv2.imdecode(image, cv2.IMREAD_COLOR)

# Reading an image from local
# image = cv2.imread('path/filename.jpg')

# Resize image
img = cv2.resize(image, (540, 540))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # To gray

# Run model
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3, minSize=(3, 3))

# Drawing the box
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    blur_region = img 
    blur_region[y:y+h, x:x+w] = cv2.blur(blur_region[y:y+h, x:x+w], (23, 23))

# Show image
cv2.imshow('imagen', blur_region)
cv2.waitKey(0)

# Save the image
cv2.imwrite('/path/image.jpg', blur_region)
