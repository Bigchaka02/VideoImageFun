import numpy as np
import cv2
import filters


#backSub = cv2.createBackgroundSubtractorMOG2()
backSub = cv2.createBackgroundSubtractorKNN()

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))

cap = cv2.VideoCapture(0)
effect = 0

while(True):
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    width = int(cap.get(3))  # float
    height = int(cap.get(4))  # float

    tmp_frame = np.zeros((height, width, 3), np.uint8)

    tmp_grey = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    tmp_invert = cv2.bitwise_not(tmp_grey)
    tmp_zeros = np.zeros((height, width), np.uint8)
    if effect == 0:
        tmp_frame = frame
    if effect == 1: # purple
        tmp_frame[:, :, 0] = tmp_grey
        tmp_frame[:, :, 1] = tmp_zeros
        tmp_frame[:, :, 2] = tmp_grey
    elif effect == 2: # red and blue
        tmp_frame = filters._xpro2(frame)
    elif effect == 3: # sepia
        m_sepia = np.asarray([[0.272, 0.534, 0.131],
                              [0.349, 0.686, 0.168],
                              [0.393, 0.769, 0.189]])
        tmp_frame = cv2.transform(frame, m_sepia)
    elif effect == 4: # blur
        tmp_frame = cv2.GaussianBlur(frame, (13, 13), 1)
    elif effect == 5:  # sharpen img
        sharp = np.asarray([[-1, -1, -1],
                            [-1, 9, -1],
                            [-1, -1, -1]])
        tmp_frame = cv2.filter2D(frame, -1, sharp)
    elif effect == 6:  # emboss img
        emboss = np.asarray([[0, -1, -1],
                            [1, 0, -1],
                            [1, 1, 0]])
        tmp_frame = cv2.filter2D(frame, -1, emboss)
    elif effect == 7:
        tmp_frame = filters._cartoon2(frame)
    elif effect == 8:
        tmp_frame = filters._clarendon(frame)
    elif effect == 9:
        tmp_frame = filters._kelvin(frame)
    elif effect == 10:
        tmp_frame = filters._warming(frame)
    elif effect == 11:
        tmp_frame = filters._cooling(frame)
    elif effect == 12:
        temp = cv2.resize(frame, (23, 23), interpolation=cv2.INTER_LINEAR)
        tmp_frame = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)
    elif effect == 13:
        ret, thresh1 = cv2.threshold(tmp_grey, 50, 255, cv2.THRESH_BINARY)
        kernel = np.ones((5, 5), np.uint8)
        erosion = cv2.erode(thresh1, kernel, iterations=1)
        opening = cv2.morphologyEx(erosion, cv2.MORPH_OPEN, kernel)
        closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
        tmp_frame = closing
    elif effect == 14:
        tmp_frame = backSub.apply(frame)
        #tmp_frame = cv2.bilateralFilter(tmp,9,75,75)
        tmp_frame = cv2.GaussianBlur(tmp_frame, (23, 23), 1)
        #ttmp_frame = cv2.medianBlur(tmp_frame, 5)
    elif effect == 15:
        ret, thresh = cv2.threshold(tmp_grey, 127, 255, 0)
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(tmp_frame, contours, -1, (255,255,255), 3)
    elif effect == 16:
        #
        tmp_frame = backSub.apply(frame)
        tmp_frame = cv2.GaussianBlur(tmp_frame, (13, 13), 1)
        ret, tmp_frame = cv2.threshold(tmp_frame, 0, 255, 0)

        #tmp_frame = cv2.borderInterpolate(tmp_frame, 5, )
        contours, hierarchy = cv2.findContours(tmp_frame, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(frame, contours, -1, (255,255,255), 3)
        #tmp_frame = cv2.GaussianBlur(tmp_frame, (13, 13), 1)

        #tmp_frame = cv2.medianBlur(tmp_frame, 5)
        #tmp_frame = cv2.bilateralFilter(tmp_frame, 9, 75, 75)
        #tmp_frame = cv2.GaussianBlur(tmp_frame, (13, 13), 1)

        #tmp_frame = cv2.morphologyEx(tmp_frame, cv2.MORPH_OPEN, kernel)





    #Display the resulting frame
    cv2.imshow('frame', tmp_frame)

    key = cv2.waitKey(1) & 0xFF
    #quit
    if key == ord('q'):
        break
    # no filter
    elif key == ord('0'):
        effect = 0
    # purple filter
    elif key == ord('1'):
        effect = 1
    # dim light
    elif key == ord('2'):
        effect = 2
    # sepia filter
    elif key == ord('3'):
        effect = 3
    # blur image
    elif key == ord('4'):
        effect = 4
    # sharpen image
    elif key == ord('5'):
        effect = 5
    # blacken image
    elif key == ord('6'):
        effect = 6
    # cartoon filter
    elif key == ord('7'):
        effect = 7
    # deepen image
    elif key == ord('8'):
        effect = 8
    # orange filter
    elif key == ord('9'):
        effect = 9
    # warm filter
    elif key == ord('w'):
        effect = 10
    # cool filter
    elif key == ord('c'):
        effect = 11
    # pixelate
    elif key == ord('p'):
        effect = 12
    # black/white
    elif key == ord('q'):
        effect = 13
    # ghost
    elif key == ord('g'):
        effect = 14
    # white outline
    elif key == ord('o'):
        effect = 15
    # test
    elif key == ord('t'):
        effect = 16


    # When everything done, release the capture
cap.release()
cv2.destroyAllWindows()