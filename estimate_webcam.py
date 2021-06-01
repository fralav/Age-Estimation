import cv2
from setup import classify_age

capture = cv2.VideoCapture(0)
if (capture.isOpened() == False):
    print("[ERRORE] Si è verificato un errore con la videocamera!")
while(capture.isOpened()):
    ret, frame = capture.read()
    cv2.putText(frame, 'Premi \'q\' per chiudere', (10, 20), cv2.FONT_ITALIC, 0.5, (0, 0, 255), 1, cv2.LINE_4)
    if (ret == True):
        age_image = classify_age(frame)
        cv2.imshow("Age Estimation - Webcam", age_image)
        if (cv2.waitKey(1) & 0xFF == ord('q')):
            break
    else:
        break
capture.release()
cv2.destroyAllWindows()