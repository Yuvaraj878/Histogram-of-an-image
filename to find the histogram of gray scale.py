hist=cv2.calcHist([gray_img],[0],None,[256],[0,256])
plt.figure()
plt.title("Histogram")
plt.xlabel("grayscale value")
plt.ylabel("pixel count")
plt.stem(hist)
plt.show()