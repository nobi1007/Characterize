# -*- coding: utf-8 -*-
"""
Created on Wed May  1 15:10:17 2019

@author: Shyam Mittal
"""
import cv2
import numpy as np

characters = list("##  @@..  ")

#characters = list(".....     ")
height = 80
width = 80

x = cv2.imread('characterize_A.jpg',0) # change the file location as per your need

array_x = np.array(x)
resized_image = cv2.resize(x,(80,50))

print(np.shape(np.array(resized_image)))
for i in range(0,50):
    for j in range(80):
        if 0 <= resized_image[i][j] <= 26:
            print(characters[0],end="")
        elif 27 <= resized_image[i][j] <= 52:
            print(characters[1],end="")
        elif 53 <= resized_image[i][j] <= 78:
            print(characters[2],end="")
        elif 79 <= resized_image[i][j] <= 104:
            print(characters[3],end="")
        elif 105 <= resized_image[i][j] <= 130:
            print(characters[4],end="")
        elif 131 <= resized_image[i][j] <= 156:
            print(characters[5],end="")
        elif 157 <= resized_image[i][j] <= 182:
            print(characters[6],end="")
        elif 183 <= resized_image[i][j] <= 206:
            print(characters[7],end="")
        elif 207 <= resized_image[i][j] <= 230:
            print(characters[8],end="")
        elif 231 <= resized_image[i][j] <= 255:
            print(characters[9],end="")
    print("",end="\n")
    
cv2.imshow('Letter A',resized_image)
cv2.waitKey(300)
cv2.destroyAllWindows()
