import cv2 as cv

capture = cv.VideoCapture('Videos/dog.mp4') #VideoCapture() method takes in the video from or system (0) for the video from the webcam and (1) for the video from the camera that is connected first on the computer and so on
while True:
    isTrue, frame = capture.read()#reads the video from the path frame by frame
    cv.imshow('Video',frame)#It displays the frame in a new window namely Video
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()

cv.destroyAllWindows()
