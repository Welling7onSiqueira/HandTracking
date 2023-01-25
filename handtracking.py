import cv2
import mediapipe as mp

camera = cv2.VideoCapture(0)
mpMao = mp.solutions.hands
mao = mpMao.Hands()
desenho = mp.solutions.drawing_utils

if camera.isOpened():
    validacao, frame = camera.read()
    while validacao:
        validacao, frame = camera.read()
        #OpenCV trablha na escala BGR
        #Converte a imagem para RGB, que é a escala utilizada pelo mediapipe
        frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) 

        #Identificação da Mão
        frameProcessado = mao.process(frameRGB)
        #print(frameProcessado.multi_hand_landmarks) #Verificar se está indentificando o movimento da mão

        if frameProcessado.multi_hand_landmarks:
            for artiMao in frameProcessado.multi_hand_landmarks:
                desenho.draw_landmarks(frame, artiMao, mpMao.HAND_CONNECTIONS)
        cv2.imshow("Imagem", frame)
        keyFrame = cv2.waitKey(5)
        if keyFrame == 27:
            break


camera.release()
cv2.destroyAllWindows()