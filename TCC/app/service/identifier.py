import cv2 as cv
from app.service.capturaFrame import captura_frame

def identifier(id):
    frame = captura_frame(id)
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    classifier = cv.CascadeClassifier(r'app/utils/haarcascade_car.xml')

    cars = classifier.detectMultiScale(gray, 1.4, 2)

    if len(cars) > 1: 
        result = 1 #True
    else:
        result = 0 #False

    return result

    