import cv2 as cv

camera = cv.VideoCapture("")

if camera.isOpened():
    conectado, frame = camera.read()

    while conectado:
        conectado, frame = camera.read()
        cv.imshow(f"Camera {id}", frame) #Abre uma janela com a imagem coletada
        key = cv.waitKey(3)
        if key == 27:
            break

camera.release()
cv.destroyAllWindows()
