import cv2
from setup import classify_age

image_path = input("Inserisci il path dell'immagine: ")
image = cv2.imread(image_path)
age_image = classify_age(image)
cv2.imshow("Age Estimation - Image", age_image)
cv2.waitKey(0)