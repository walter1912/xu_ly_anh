import numpy as np
import cv2
# khởi tạo mảng NumPy với method np.zeros() với x=300px, y=300px ;dtype="uint8" để biểu diễn hình ảnh dưới dạng màu RGB
canvas = np.zeros((300, 300, 3), dtype = "uint8")
# tạo màu green
green = (0, 255, 0)
# vẽ vào bảng canvas 1 đường thẳng màu green với điểm bắt đầu là (x=0,y=0) điểm kết thúc là (x=300, y=300) 
cv2.line(canvas, (0, 0), (300, 300), green)
# show canvas sau khi vẽ
cv2.imshow("Canvas", canvas)
# nhấn phím bất kì để chương trình tiếp tục chạy
cv2.waitKey(0)
# tạo màu red
red = (0, 0, 255)
# vẽ vào bảng canvas 1 đường thẳng màu red với điểm bắt đầu là (x=300,y=0) điểm kết thúc là (x=0, y=300) độ dày=3px
cv2.line(canvas, (300, 0), (0, 300), red, 3)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
# vẽ vào bảng canvas 1 hình chữ nhật màu green với điểm bắt đầu là (x=10,y=10) điểm kết thúc là (x=60, y=60) 
cv2.rectangle(canvas, (10, 10), (60, 60), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
# vẽ vào bảng canvas 1 hình chữ nhật màu red với điểm bắt đầu là (x=50,y=200) điểm kết thúc là (x=200, y=225) độ dày=10px
 
cv2.rectangle(canvas, (50, 200), (200, 225), red, 10)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

blue = (255, 0, 0)
# vẽ vào bảng canvas 1 hình chữ nhật màu blue với điểm bắt đầu là (x=200,y=50) điểm kết thúc là (x=225, y=125) độ dày=100% 
cv2.rectangle(canvas, (200, 50), (225, 125), blue, -1)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)


# tạo canvas mới để vẽ hình tròn
canvas = np.zeros((300, 300, 3), dtype = "uint8")
# tạo tọa độ ở chính giữa canvas
(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)
# tạo màu trắng
white = (255, 255, 255)
# dùng vòng for vẽ 7 vòng tròn có bán bính từ 0 đến 175 
for r in range(0, 175, 25):
    # dùng method circle(canvas, tọa độ tâm, bán kính, màu sắc) để vẽ
    cv2.circle(canvas, (centerX, centerY), r, white)
# show ra màn hình canvas sau khi được vẽ
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
# vẽ 25 lần
for i in range(0, 25):
    # random 1 bán kính bất kì từ 5 đến 200px
    radius = np.random.randint(5, high = 200)
    # chọn ra 1 màu bất kì theo thang rgb
    color = np.random.randint(0, high = 256, size = (3,)).tolist()
    # tạo ra 1 tọa độ tâm bất kì
    pt = np.random.randint(0, high = 300, size = (2,))
    # vẽ hình tròn với độ dày = 100%
    cv2.circle(canvas, tuple(pt), radius, color, -1)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)