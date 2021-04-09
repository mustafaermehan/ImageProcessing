import cv2
import numpy as np

#create an image
img = np.zeros((512,512,3),np.uint8) # black image
print(img.shape)

cv2.imshow("Siyah",img)

#line 
cv2.line(img, (0,0),(512,512),(0,255,0),3) # (resim,başlangıç noktası,bitiş noktası, renk,kalınlık)
cv2.imshow("Cizgi",img)

#Rectangle
#(resim, başlangıç,bitiş,renk)
cv2.rectangle(img, (0,0),(256,256),(255,0,0),cv2.FILLED)
cv2.imshow("Rectangle",img)

#cember
#(resim,merkez,yarı çap,renk)
cv2.circle(img, (300,300),45,(0,0,255), cv2.FILLED)
cv2.imshow("Circle",img)

#text
#(resim, başlangıç, font, kalınlık, renk)
cv2.putText(img,"Resim",(350,350), cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255))
cv2.imshow("Text",img)