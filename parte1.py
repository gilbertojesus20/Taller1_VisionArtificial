import cv2
from os import path
from taller1 import cartoonize

file_path = path.abspath(path.dirname(__file__))
rgb_image = cv2.imread('FB_IMG_1607469881416.jpg')

pasos = cartoonize(rgb_image)

for i, paso in enumerate(pasos):
    cv2.imwrite(path.join(file_path, 'Paso{}.png'.format(i+1)), paso)



#hola este es un cambio jaja para