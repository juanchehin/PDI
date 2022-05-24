# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
import cv2

image_filename = '1.jpeg'

full_image_path = os.path.join("C:\Programacion\PDI\practica", image_filename)

img = cv2.imread(full_image_path)


cv2.imshow("ventana1",img)

cv2.waitKey()