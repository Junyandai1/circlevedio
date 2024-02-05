import cv2
import numpy as np

# read video
cap = cv2.VideoCapture(r"C:\Users\xjucsy\Desktop\rolling_can.mp4")  # VideoCapture(video_path)

ret, frame = cap.read() # read video capture, 
# ret is the status of first frame; frame is the image of first frame

while True:   # while video is still handling 
    ret, frame = cap.read() # read next frame
    
    if not ret or frame is None:    # if read error or frame is not read correctly:
        break                       # end program
    
    # convert frame to gray image
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detect circles in this frame
    circles = cv2.HoughCircles(gray, 
                               cv2.HOUGH_GRADIENT, 
                               dp=1, 
                               minDist=100, 
                               param1=100, 
                               param2=50, 
                               minRadius=0, 
                               maxRadius=1500)

    # overlay circles on the original frame
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int") # convert float data to int
        (x, y, r) = circles[0]  # find the circle with biggest probility
        cv2.circle(frame, (x, y), r, (0, 255, 0), 4)    # draw circle line
        cv2.circle(frame, (x, y), 4, (0, 255, 0), -1)   # draw circle canter

    # show image w/ circle per frame
    cv2.imshow('rolling_can circle detected window', frame) # show frame in a window
    key = cv2.waitKey(1)    # "waitKey(n)" means wait for keyboard input in n ms
    
    if key == ord('q'): # if you input 'q' anytime,
        break   # the program will exit at once.
        
cap.release()   # release video capture
cv2.destroyAllWindows()  # release windows

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