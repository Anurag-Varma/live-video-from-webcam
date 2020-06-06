import cv2

cap = cv2.VideoCapture(0)

while(cap.isOpened()):

    print ("opened")
    ret, frame = cap.read()

    cv2.imshow('Live', frame)
    if cv2.waitKey(25) & 0xFF == 27: #enter esc to exit from the camera
        print("break")
        break

cap.release()

cv2.destroyAllWindows()

print ("end")