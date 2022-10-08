import numpy as np
import cv2
cap = cv2.VideoCapture(0)

def color(c):
    r=0
    g=0
    b=0
    while c>360:
        c-=360
    if 0<=c and c<60:
        r=255
        g=int(255*c/60)
    if 60<=c and c<120:
        r=int(255*(120-c)/60)
        g=255
    if 120<=c and c<180:
        g=255
        b=int(255*(c-120)/60)
    if 180<=c and c<240:
        g=int(255*(240-c)/60)
        b=255
    if 240<=c and c<300:
        r=int(255*(c-240)/60)
        b=255
    if 300<=c and c<=360:
        r=255
        b=int(255*(360-c)/60)
    return r,g,b

x=50
y=50
dx=5
dy=5


while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    width = cap.get(3)
    length = cap.get(4)

    x+=dx
    y+=dy

    rad = 50

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.flip(frame, 1)
    frame = cv2.circle(frame, (x,y), rad, color(x/3 ), -1)


    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord(' '):
        break

    if x-rad<0 or x+rad>width:
        dx*=-1
    if y-rad<0 or y+rad>length:
        dy*=-1


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()