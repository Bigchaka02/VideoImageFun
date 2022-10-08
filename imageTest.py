# pip3 install numpy
# pip3 install opencv-python
# pip3 install matplotlib

# import a library
import numpy as np
import cv2

# load a color image in greyscale
img = cv2.imread("babyYoda.jpeg",0)

#cv2.imshow('image', img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

img = cv2.line(img,(0,0),(511,511),0,5)

print(img)


#using matplotlib
from matplotlib import pyplot as plt

plt.imshow(img, cmap = 'gray')
plt.show()

