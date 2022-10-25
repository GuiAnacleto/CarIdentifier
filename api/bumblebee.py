import cv2 as cv

def captura_video():
    '''Função que captura a live da camera para a analise'''
    camera = cv.VideoCapture("")

    if camera.isOpened():
        conectado, frame = camera.read()

        while conectado:
            conectado, frame = camera.read()
            cv.imshow(f"Camera {id}", frame) #Abre uma janela com a imagem coletada
            key = cv.waitKey(3)
            if key == 27:
                break
    #cv.imwrite("deagora.png", frame) #Teste do frame capturado
    camera.release()
    cv.destroyAllWindows()


def captura_frame(id):
    '''Função que captura o frame para a analise'''

    if id == 0:
        camera = cv.VideoCapture("")
        cv.waitKey(1)
    elif id == 1:
        camera = cv.VideoCapture("")
        cv.waitKey(1)
    else:
        frame = cv.imread('imagem-com-carro.jpg')
        cv.waitKey(1)
        return frame

    frame = camera.read()
    camera.release()
    cv.destroyAllWindows()

    return frame[1]

def identifier(id):
    frame = captura_frame(id)
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    classifier = cv.CascadeClassifier('haarcascade_car.xml')

    cars = classifier.detectMultiScale(gray, 1.4, 2)

    if len(cars) > 1: 
        result = True
    else:
        result = False

    return result


    