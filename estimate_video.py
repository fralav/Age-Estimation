import cv2
from setup import classify_age

video_path = input("Inserisci il path del video: ")
capture = cv2.VideoCapture(video_path)
if (capture.isOpened() == False):
    print("[ERRORE] Si è verificato un errore nell'apertura del video!")
while(capture.isOpened()):
    ret, frame = capture.read()
    cv2.putText(frame, 'Premi \'q\' per chiudere', (10, 20), cv2.FONT_ITALIC, 0.5, (0, 0, 255), 1, cv2.LINE_4)
    if (ret == True):
        age_video = classify_age(frame)
        cv2.imshow("Age Estimation - Video", age_video)
        if (cv2.waitKey(1) & 0xFF == ord('q')):
            break
    else:
        break
capture.release()
cv2.destroyAllWindows()