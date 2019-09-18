import cv2

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)
vc.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
vc.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()


else:
    rval = False

while rval == True :
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # cv2.imshow("preview", gray)
    # cv2.imshow('second preview', frame)
    # rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break
cv2.destroyWindow("preview")