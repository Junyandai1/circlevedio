import cv2
import numpy as np

# read video
cap = cv2.VideoCapture("/Users/daijunyan/Desktop/jy 2024-02-02 21.11.02.mp4")

ret, frame = cap.read()

while True:
    ret, frame = cap.read()

    if not ret or frame is None:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    circles = cv2.HoughCircles(gray,
                               cv2.HOUGH_GRADIENT,
                               dp=1,
                               minDist=100,
                               param1=100,
                               param2=50,
                               minRadius=0,
                               maxRadius=1500)

    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        (x, y, r) = circles[0]
        cv2.circle(frame, (x, y), r, (0, 255, 0), 4)
        cv2.circle(frame, (x, y), 4, (0, 255, 0), -1)

    cv2.imshow('rolling_can circle detected window', frame)
    key = cv2.waitKey(1)

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

'''
pseudo code for detecting circle in rolling can:

1   videoCapture = readVideo(videoPath)
2   while next frame existing:
3       frame = readFrame(videoCapture)
4       gray_frame = cvtColor(frame)
5       circles = detectCircle(gray_frame)
6       overlay(frame, circles[0])
7       showFrame(frame)
8       key = waitKey(1)
9       exit if key == 'q'
10  release(videoCapture)
'''
