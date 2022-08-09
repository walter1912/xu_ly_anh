import numpy as np
import argparse
import cv2
print(cv2.__version__)
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
help = "Path to the image")
args = vars(ap.parse_args()) 
# đọc ảnh từ file
image = cv2.imread(args["image"])
# hiển thị ra ảnh gốc
cv2.imshow("Original", image)
cv2.waitKey(0)
# tạo ảnh mới với không gian màu xám từ method cvtColor(ảnh, màu)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)
cv2.waitKey(0)
# tạo ảnh mới với không gian nàu hsv 
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)
cv2.waitKey(0)
# tạo ảnh mới với không gian màu lab
lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
cv2.imshow("L*a*b*", lab)
cv2.waitKey(0)
