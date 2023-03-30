import cv2
import matplotlib.pyplot as plt
gray_img=cv2.imread("img2.jpg",0)
color_img=cv2.imread("img1.jpg",-1)
gray_img=cv2.cvtColor(gray_img,cv2.COLOR_BGR2RGB)
color_img=cv2.cvtColor(color_img,cv2.COLOR_BGR2RGB)
plt.title("Color Image")
plt.axis("off")
plt.imshow(color_img)
plt.show()
plt.title("Gray Scale Image")
plt.axis("off")
plt.imshow(gray_img)
plt.show()
