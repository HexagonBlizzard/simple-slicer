import cv2
import numpy as np
from math import floor
imgPath = input('Укажите путь до изображения: ')
imgName = input('Укажите название изображения: ')
img = cv2.imread(imgPath + imgName, cv2.IMREAD_UNCHANGED)
x = floor(float(input('Введите x: ')))
y = floor(float(input('Введите y: ')))
temp = np.zeros((floor(img.shape[0]/x), floor(img.shape[1]/y),4), np.uint8)
for i in range(x):
    for j in range(y):
        temp = img[floor(img.shape[0]/x)*i:floor(img.shape[0]/x)*(i+1), floor(img.shape[1]/y)*j:floor(img.shape[1]/y)*(j+1)]
        cv2.imwrite(imgPath + str(i+j*x) + '.png', temp)