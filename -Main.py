import cv2
import dlib
import imutils
from imutils import face_utils

# Inicializar o detector de faces do dlib
detector = dlib.get_frontal_face_detector()

# Inicializar o modelo de pontos faciais do dlib
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

# Função para detectar e desenhar os pontos faciais e retângulo na imagem
def draw_landmarks(image, shape, face_rect):
    for (x, y) in shape:
        cv2.circle(image, (x, y), 1, (255, 255, 0), -1)
    (x, y, w, h) = face_rect
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Inicializar a captura de vídeo
video_capture = cv2.VideoCapture(0)

while True:
    # Ler o próximo quadro de vídeo
    ret, frame = video_capture.read()

    # Redimensionar o quadro para melhor desempenho
    frame = imutils.resize(frame, width=800)

    # Converter o quadro para escala de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar as faces no quadro
    faces = detector(gray)

    for face in faces:
        # Prever os pontos faciais e retângulo para a face atual
        shape = predictor(gray, face)
        shape = face_utils.shape_to_np(shape)
        (x, y, w, h) = face.left(), face.top(), face.width(), face.height()

        # Desenhar os pontos faciais e retângulo na imagem
        draw_landmarks(frame, shape, (x, y, w, h))

    # Mostrar o quadro com os pontos faciais e retângulo
    cv2.imshow('Pontos Faciais', frame)

    # Verificar se a tecla 'q' foi pressionada para sair do loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar os recursos
video_capture.release()
cv2.destroyAllWindows()
