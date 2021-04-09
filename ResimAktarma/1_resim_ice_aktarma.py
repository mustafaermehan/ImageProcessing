import cv2

#ice aktarma

img = cv2.imread("messi5.jpg",0)

#gorsellestirme
cv2.imshow("ilk resim",img)

k = cv2.waitKey(0) &0xFF

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite("messi_gray.png", img)
    cv2.destroyAllWindows()