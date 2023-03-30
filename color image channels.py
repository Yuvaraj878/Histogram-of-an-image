
# Developed By: YUVARAJ.S
# Register Number:22008589
hist=cv2.calcHist([color_img],[0],None,[256],[0,256])
plt.title("Histogram of Color Image:Red Channel")
plt.xlabel("Intensity value")
plt.ylabel("pixel count")
plt.stem(hist)
plt.show()