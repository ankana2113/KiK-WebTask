import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# The default size of frame from camera will be 640x480 in Windows
# we will set it to 1280x480
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# cap.isOpened() true/false
print(cap.isOpened())

# cap.read()


while cap.isOpened():
    ret_flag, img_camera = cap.read()

    cv2.imshow("camera", img_camera)

    # wait for 1 millisecond
    k = cv2.waitKey(1)

    # capture screenshot
    if k == ord('s'):
        cv2.imwrite("test.jpg", img_camera)

    # exit program on pressing 'q'
    if k == ord('q'):
        break

# release video
cap.release()

# destroy window after all is done
cv2.destroyAllWindows()
