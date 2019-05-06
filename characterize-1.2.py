# -*- coding: utf-8 -*-
"""
Created on Wed May  1 15:10:17 2019

@author: Shyam Mittal
"""
# these variables can be changed
height = 70
width = 120
character = '@'

import cv2
import numpy as np
from hex_color_codes2 import codes
from sklearn.neighbors import NearestNeighbors

#from colored import fg,attr

all_colors_list = []

for i in codes:
    temp = []
    for j in range(1,7,2):
        temp.append(int(i[j]+i[j+1],16))
    all_colors_list.append(tuple(temp))
all_colors = np.array(all_colors_list)
    
x = cv2.imread('characterize_github.jpg') #change the file location to your required image

new_x = cv2.resize(x,(width,height))

color_dict = {}
color_check_arr = []

for i in range(height):
    temp_to_cca = []
    for j in range(width):
        hex_value = "#%02x%02x%02x"%tuple(new_x[i][j])
        if hex_value in codes:
            temp_to_cca.append(hex_value)
        else:
            if not tuple(new_x[i][j]) in list(color_dict.keys()):    
                all_colors_list.append(tuple(new_x[i][j]))
                all_colors = np.array(all_colors_list)
                nbrs = NearestNeighbors(n_neighbors=2, algorithm='ball_tree').fit(all_colors)
                distances,indices = nbrs.kneighbors(all_colors)
                temp_calac_val = all_colors_list[indices[247][1]]
                hex_value = "#%02x%02x%02x"%temp_calac_val
                color_dict[tuple(new_x[i][j])] = hex_value
                all_colors_list = all_colors_list[:-1]
            temp_to_cca.append(hex_value)
    color_check_arr.append(temp_to_cca)

f = open("characterize-main.html",'w+')
part1 = """
<html>
<head>
<title>hghgc</title>
<style>
body{   
font-size:5px;
background-color:black;
}
</style>
</head>
<body>"""

part2 = """"""

for i in range(height):
    for j in range(width):
        part2 += """<span style='color:%s'>%s</span>"""%(color_check_arr[i][j],character)
        #print(color_check_arr[i][j])
    part2 += """</br>"""
part3 = """
</body>
</html>"""

fr = f.writelines(part1+part2+part3)
f.close()

print(np.shape(new_x))
cv2.imshow("Github_logo",new_x)
cv2.waitKey(100)
cv2.destroyAllWindows()
