import numpy as np
import cv2
from tensorflow.keras.models import load_model

age_ranges = ['1-2', '3-9', '10-20', '21-25', '26-27', '28-31', '32-36', '37-45', '46-54', '55-65', '66-116']
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
model = load_model('model.h5')


def reduce_roi(x, y, w, h):
    x_new = int(x + (w * 0.05))
    y_new = int(y + (h * 0.05))
    w_new = int(w * 0.9)
    h_new = int(h * 0.9)
    return x_new, y_new, w_new, h_new


def create_text(image, age_text, pred_text, x, y, w, h):
    (age_text_w, age_text_h), age_text_baseline = cv2.getTextSize("Eta': " + age_text, fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, thickness=2)
    (pred_text_w, pred_text_h), pred_text_baseline = cv2.getTextSize(pred_text, fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.65, thickness=1)
    x_center = x + (w / 2)
    y_age_text_center = y + h + 20
    y_pred_text_center = y + h + 48
    x_age_text = int(round(x_center - (age_text_w / 2)))
    y_age_text = int(round(y_age_text_center + (age_text_h / 2)))
    x_pred_text = int(round(x_center - (pred_text_w / 2)))
    y_pred_text = int(round(y_pred_text_center + (pred_text_h / 2)))
    cv2.rectangle(image, (x - 1, y + h), (x + w + 1, y + h + 64), (0, 0, 255), cv2.FILLED)
    cv2.putText(image, "Eta': " + age_text, org=(x_age_text, y_age_text), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, thickness=2, color=(0, 0, 0), lineType=cv2.LINE_AA)
    cv2.putText(image, pred_text, org=(x_pred_text, y_pred_text), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.65, thickness=1, color=(0, 0, 0), lineType=cv2.LINE_AA)


def classify_age(image):
    image_copy = np.copy(image)
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(image_copy, scaleFactor=1.4, minNeighbors=6, minSize=(100, 100))
    for i, (x, y, w, h) in enumerate(faces):
        cv2.rectangle(image_copy, (x, y), (x + w, y + h), (255, 255, 255), thickness=2)
        x2, y2, w2, h2 = reduce_roi(x, y, w, h)
        roi = image_gray[y2:y2 + h2, x2:x2 + w2]
        roi = cv2.resize(roi, (200, 200))
        roi = roi.reshape(-1, 200, 200, 1)
        age_text = age_ranges[np.argmax(model.predict(roi))]
        pred_text = f"Precisione: {round(np.max(model.predict(roi)) * 100, 2)}%"
        create_text(image_copy, age_text, pred_text, x, y, w, h)
    return image_copy
