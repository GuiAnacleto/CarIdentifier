import cv2 as cv
import os

def captura_frame(id):
    '''Função que captura o frame para a analise'''

    if id == 0:
        camera = cv.VideoCapture("")
        cv.waitKey(1)
    elif id == 1:
        camera = cv.VideoCapture("")
        cv.waitKey(1)
    else:
        print(f"else sem carro {os.getcwd()}")
        frame = cv.imread(r'app/utils/pexels-charles-kettor-1077785.jpg')
        cv.waitKey(1)
        return frame

    frame = camera.read()
    camera.release()
    cv.destroyAllWindows()

    return frame[1]
