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