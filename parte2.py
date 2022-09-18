import cv2
from os import path, mkdir
from taller1 import cartoonize

file_path = path.abspath(path.dirname(__file__))
out_path = path.join(file_path, 'out')

if not path.isdir(out_path):
  mkdir(out_path)

# Capturar desde la camara web
video_capture = cv2.VideoCapture(0)
frame_index = 0

ret, frame = video_capture.read()
cv2.imshow('OpenCV Segmentacion de Color', frame)

while True:
  # iniciar captura
  ret, frame = video_capture.read()
  # TODA MODIFICACION A LA IMAGEN DE ENTRADA
  # SE DEBE COLOCAR EN ESTA PARTE DEL CODIGO
  #
  final_image = cartoonize(frame)[-1]
  # Presionar C para guardar
  if cv2.waitKey(20) & 0xFF == ord('c'):
    frame_name = "camera_frame_{}.png".format(frame_index)
    frame_path = path.join(out_path, frame_name)
    if not cv2.imwrite(frame_path, final_image):
      raise Exception("Error al escribir la imagen")
    frame_index += 1
    cv2.imshow('OpenCV Segmentacion de Color', final_image)
  # Presionar 'q' para salir
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
video_capture.release()
cv2.destroyAllWindows()