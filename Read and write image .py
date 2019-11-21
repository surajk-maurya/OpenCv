import cv2                   # import openCv library
img=cv2.imread('lena.jpg',1) #read lena.jpg in: greyscale=0, colour=1, unchanged=-1  

print(img)                   #print the image in matrix form

cv2.imshow('image',img)      #show 'img' variable in image form to wait the the program for 5 sec at the image window

k=cv2.waitKey() & 0xFF
if k==27:
 cv2.destreoyAllwindows()
elif k== ord('s'):
 cv2.imwrite('lena_copy.png',img) #copy  the 'img' variable in in png formate

