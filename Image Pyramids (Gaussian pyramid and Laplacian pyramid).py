import cv2
import numpy as np 


img = cv2.imread('lena.jpg')
PrD1 = cv2.pyrDown(img)
PrD2 = cv2.pyrDown(PrD1)

PrUp1 = cv2.pyrUp(img)



cv2.imshow('Original Image', img)
cv2.imshow('Pr1', PrD1)
cv2.imshow('PrD2', PrD2)
cv2.imshow('PrUp', PrUp1)


cv2.waitKey(0)
cv2.destroyAllWindows()


#===============*============#

#####Gaussian pyramid 



import cv2
import numpy as np 

img = cv2.imread('lena.jpg')

#to copy my img in this variable
layer = img.copy()
#gaussian pyramid contains my img in list
gp =[layer]


for i in range(6):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    cv2.imshow(str(i),layer)
    
    
cv2.imshow('Original Image', img)    
    

cv2.waitKey(0)
cv2.destroyAllWindows()




#==============*=============#

###### Laplacian pyramid

import cv2

import numpy as np

img = cv2.imread("lena.jpg")

layer = img.copy()

gaussian_pyramid_list = [layer]



for i in range(6):

    layer = cv2.pyrDown(layer)     

    gaussian_pyramid_list.append(layer)     

    #cv2.imshow(str(i), layer)     



layer = gaussian_pyramid_list[5]

cv2.imshow('upper level Gaussian Pyramid', layer)

laplacian_pyramid_list = [layer]



for i in range(5, 0, -1):

    gaussian_extended = cv2.pyrUp(gaussian_pyramid_list[i])     

    laplacian = cv2.subtract(gaussian_pyramid_list[i-1], gaussian_extended)     

    cv2.imshow(str(i), laplacian)     



cv2.imshow("Original image", img)

cv2.waitKey(0)

cv2.destroyAllWindows()
