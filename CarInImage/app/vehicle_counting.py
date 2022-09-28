import cv2
import glob
from vehicle_detector import VehicleDetector

# Load Veichle Detector
vd = VehicleDetector()

def cars_count(img_path):
    vehicles_folder_count = 0
    img = cv2.imread(img_path)

    vehicle_boxes = vd.detect_vehicles(img)
    vehicle_count = len(vehicle_boxes)    

    for box in vehicle_boxes:
        x, y, w, h = box

        cv2.rectangle(img, (x, y), (x + w, y + h), (25, 0, 180), 3)

        cv2.putText(img, "Vehicles: " + str(vehicle_count), (20, 50), 0, 2, (100, 200, 0), 3)

    return vehicle_count

def cars_count_folder(img_path):

    vehicles_folder_count = 0

    for img_path in images_folder:
        print("Img path", img_path)
        img = cv2.imread(img_path)

        vehicle_boxes = vd.detect_vehicles(img)
        vehicle_count = len(vehicle_boxes)

        # Update total count
        vehicles_folder_count += vehicle_count

        for box in vehicle_boxes:
            x, y, w, h = box

            cv2.rectangle(img, (x, y), (x + w, y + h), (25, 0, 180), 3)

            cv2.putText(img, "Vehicles: " + str(vehicle_count), (20, 50), 0, 2, (100, 200, 0), 3)

            cv2.imshow("Cars", img)
            cv2.waitKey(1)

    return vehicles_folder_count


#cars_qtd = cars_count("images\pexels-adrien-olichon-2387615.jpg")
print(cars_count_folder("images/*.jpg"))