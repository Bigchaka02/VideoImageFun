
import cv2

# Load an color image in grayscale
img = cv2.imread('abba.png',1) #what happens when this is 1?

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.1 , 6)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 0), 2)

# #Using MatPlotLib
# from matplotlib import pyplot as plt
# plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
#
# plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
# plt.show()


cv2.imshow('image',img)
cv2.waitKey( )
cv2.destroyAllWindows()
