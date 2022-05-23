# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 12:37:59 2022

@author: Jesus-Mtz
"""

import cv2
import numpy as np

# img = cv2.imread("coins.png")
# img2 = img.copy()
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# _, th = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
# kernel = np.ones((3,3), np.uint8)
# closing = cv2.morphologyEx(th, cv2.MORPH_CLOSE, kernel)

# contornos, jerarquia = cv2.findContours(closing, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# for index in range(len(contornos)):
#     cv2.drawContours(img2, contornos, index, (0,255,0), 5)
    
#     cnt = contornos[index]
#     M = cv2.moments(cnt)
    
#     cx = int(M['m10']/M['m00']) ## calculamos la coordenada x del centroide
#     cy = int(M['m01']/M['m00'])## calculamos la coordenada y del centroide
    
#     img = cv2.circle(img, (cx,cy), radius=2, color = (0,0,255), thickness = -1)
#     img = cv2.putText(img, "aqui va la anotacion", (cx-20,cy), 
#                       cv2.FONT_HERSHEY_SIMPLEX, .3, (255,0,0), 1, cv2.LINE_AA )
    
    
# cantidad = len(contornos)

# img2 = cv2.putText(img2, "son "+ str(cantidad)+ " monedas", (10,50),
#                     cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)

# print("Son " + str(cantidad)+ " monedas")

# cv2.namedWindow("original", cv2.WINDOW_NORMAL)
# cv2.namedWindow("closing", cv2.WINDOW_NORMAL)
# cv2.namedWindow("Resultados", cv2.WINDOW_NORMAL)
# cv2.imshow("original", img)
# cv2.imshow("closing", closing)
# cv2.imshow("Resultados", img2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# img = cv2.imread("coins.png")
# img2 = img.copy()
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# _, th = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
# kernel = np.ones((3,3), np.uint8)
# closing = cv2.morphologyEx(th, cv2.MORPH_CLOSE, kernel)

# contornos, jerarquia = cv2.findContours(closing, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# for index in range(len(contornos)):
    
#     area = cv2.contourArea(contornos[index])
    
#     cv2.drawContours(img2, contornos, index, (0,255,0), 5)
    
#     cnt = contornos[index]
#     M = cv2.moments(cnt)
    
#     cx = int(M['m10']/M['m00']) ## calculamos la coordenada x del centroide
#     cy = int(M['m01']/M['m00'])## calculamos la coordenada y del centroide
    
#     img = cv2.circle(img, (cx,cy), radius=2, color = (0,0,255), thickness = -1)
#     img = cv2.putText(img, str(area), (cx-20,cy), 
#                       cv2.FONT_HERSHEY_SIMPLEX, .3, (255,0,0), 1, cv2.LINE_AA )
    
    
# cantidad = len(contornos)

# img2 = cv2.putText(img2, "son "+ str(cantidad)+ " monedas", (10,50),
#                     cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)

# print("Son " + str(cantidad)+ " monedas")

# cv2.namedWindow("original", cv2.WINDOW_NORMAL)
# cv2.namedWindow("closing", cv2.WINDOW_NORMAL)
# cv2.namedWindow("Resultados", cv2.WINDOW_NORMAL)
# cv2.imshow("original", img)
# cv2.imshow("closing", closing)
# cv2.imshow("Resultados", img2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


img = cv2.imread("tornillos.jpg")
img2 = img.copy()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, th = cv2.threshold(gray, 230, 255, cv2.THRESH_BINARY_INV)
kernel = np.ones((3,3), np.uint8)
closing = cv2.morphologyEx(th, cv2.MORPH_CLOSE, kernel)

contornos, jerarquia = cv2.findContours(closing, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

contornosLista = []

for index in range(len(contornos)):
    
    area = cv2.contourArea(contornos[index])
    
    if area > 5000:
        contornosLista.append(contornos[index])
    
        cnt = contornos[index]
        M = cv2.moments(cnt)
        
        cx = int(M['m10']/M['m00']) ## calculamos la coordenada x del centroide
        cy = int(M['m01']/M['m00'])## calculamos la coordenada y del centroide
        
        img = cv2.circle(img, (cx,cy), radius=2, color = (0,0,255), thickness = -1)
        img = cv2.putText(img, str(area), (cx-20,cy), 
                          cv2.FONT_HERSHEY_SIMPLEX, .3, (255,0,0), 1, cv2.LINE_AA )
    
cv2.drawContours(img2, contornosLista, -1, (0,255,0), 5)   
cantidad = len(contornosLista)

img2 = cv2.putText(img2, "son "+ str(cantidad)+ " elementos", (10,50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)

print("Son " + str(cantidad)+ " monedas")

cv2.namedWindow("original", cv2.WINDOW_NORMAL)
cv2.namedWindow("closing", cv2.WINDOW_NORMAL)
cv2.namedWindow("Resultados", cv2.WINDOW_NORMAL)
cv2.imshow("original", img)
cv2.imshow("closing", closing)
cv2.imshow("Resultados", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
