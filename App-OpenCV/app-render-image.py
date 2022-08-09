from tkinter import *
from tkinter import filedialog

from PIL import Image
from PIL import ImageTk
import cv2

import imutils

import numpy as np
def choose_image():
    # Chỉ định loại tệp, để chỉ chọn hình ảnh
    path_image = filedialog.askopenfilename(filetypes = [
        ("image", ".jpeg"),
        ("image", ".png"),
        ("image", ".jpg")])
    # nếu tệp có tồn tại thì tạo biến toàn cục image
    if len(path_image) > 0:
        global image

    # Tải hình ảnh từ một tệp
        image = cv2.imread(path_image)
        # đặt lại kích thước ảnh với chiều dài là 
        image= imutils.resize(image, width=360)

    # Để hiển thị hình ảnh đầu vào trong GUI
        imageToShow= imutils.resize(image,width=360)
            # màu gốc bằng hàm cv2.COLOR_BGR2RGB
        imageToShow = cv2.cvtColor(imageToShow, cv2.COLOR_BGR2RGB)
        # Tạo bộ nhớ hình ảnh từ một đối tượng giao diện mảng (sử dụng giao thức đệm). 
        # PIL.Image. fromarray ( obj , mode = None )
        im = Image.fromarray(imageToShow )
        # PIL.ImageTk.PhotoImage(image=None, size=None, **kw)
        img = ImageTk.PhotoImage(image=im)
# tag_configure(tagname, option=None, **kw)
# truy vấn hoặc sửa đổi các tùy chọn cho tên thẻ được chỉ định .
        lblInputImage.configure(image=img)
        # lấy đường dẫn đến ảnh
        lblInputImage.image = img

    # Nhãn HÌNH ẢNH ĐẦU VÀO
        lblInfo1 = Label(root, text="HÌNH ẢNH ĐẦU VÀO:")
        # cột, hàng, pading trục x, padding trục y
        lblInfo1.grid(column=1, row=0, padx=5, pady=5)
    # khi đọc hình ảnh đầu vào, 
    # hình ảnh đầu ra và xóa lựa chọn
    # ở radiobutton
        lblOutputImage.image = ""
        lblImageRes2.image = ""
        selected.set(0)


def deteccion_color():
    global image
    if selected.get() == 1:
        # Màu đỏ
        # tạo 1 mảng màu mưc thấp 1 lowRange
        lowRange1 = np.array([0, 50, 70], np.uint8)
        # tạo 1 mảng màu mưc cao 1 highRange
        highRange1 = np.array([9, 255, 255], np.uint8)
        # tạo 1 mảng màu mưc thấp 2
        lowRange2 = np.array([159, 50, 70], np.uint8)
        # tạo 1 mảng màu mưc cao 2
        highRange2 = np.array([180, 255, 255], np.uint8)

    if selected.get() == 2:
      # Màu vàng
        # tạo 1 mảng màu mưc thấp 
        lowRange = np.array([25, 50, 70], np.uint8)
        # tạo 1 mảng màu mưc cao 
        highRange = np.array([35, 255, 255], np.uint8)

    if selected.get() == 3:
       # Màu xanh da trời
        # tạo 1 mảng màu mưc thấp 
        lowRange = np.array([90, 50, 70], np.uint8)
        # tạo 1 mảng màu mưc cao 
        highRange = np.array([128, 255, 255], np.uint8)

    # màu xanh lá cây
    if selected.get() == 4:
        lowRange = np.array([36, 50, 70], np.uint8)

        highRange = np.array([88, 255, 255], np.uint8)
    # màu cam
    if selected.get() == 5:
        lowRange = np.array([10, 50, 70], np.uint8)

        highRange = np.array([24, 255, 255], np.uint8)
  
    # màu tím
    if selected.get() == 6:
        lowRange = np.array([129, 50, 70], np.uint8)

        highRange = np.array([158, 255, 255], np.uint8)

    # tạo ảnh mới có bộ lọc màu xám lấy từ biến global image
    # chuyển từ màu bình thường thành màu xám
    imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # chuyển từ màu xám thành màu bình thường
    imageGray = cv2.cvtColor(imageGray, cv2.COLOR_GRAY2BGR)
    # chuyển từ màu bình thường thành màu HSV 
    imageHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    if selected.get() == 1:
    # Phát hiện màu đỏ
    # HÀM cv2.inRange: Kiểm tra xem các phần tử của mảng có nằm giữa các phần tử của hai mảng khác không.
    # tạo mặt nạ phát hiện màu đỏ maskRed
        maskRed1 = cv2.inRange(imageHSV, lowRange1, highRange1)
        maskRed2 = cv2.inRange(imageHSV, lowRange2, highRange2)
        # cv2.add(): Tính tổng mỗi phần tử của hai mảng hoặc một mảng và một đại lượng vô hướng.
        mask = cv2.add(maskRed1, maskRed2)
    else:
              
    # Phát hiện các màu còn lại
        mask = cv2.inRange(imageHSV, lowRange, highRange)
       
# cv2.medianBlur: Làm mờ hình ảnh bằng bộ lọc trung vị.
    mask = cv2.medianBlur(mask, 7)
    # cv2.bitwise_and: tính toán kết hợp theo từng bit của hai mảng (dst = src1 & src2) 
    # Tính toán kết hợp bit khôn ngoan trên mỗi phần tử của hai mảng hoặc một mảng và một đại lượng vô hướng.
    colorDetected = cv2.bitwise_and(image, image, mask=mask)

    # Nền xám
    # cv2.bitwise_not: Đảo ngược từng bit của một mảng.
    invMask = cv2.bitwise_not(mask)
    bgGray = cv2.bitwise_and(imageGray, imageGray, mask=invMask)

    # Thêm bgGray và colorDetected
    finalImage = cv2.add(bgGray, colorDetected)
    imageToShowOutput = cv2.cvtColor(finalImage, cv2.COLOR_BGR2RGB)

    # Để hiển thị hình ảnh trong lblOutputImage trong GUI
    im = Image.fromarray(imageToShowOutput)
    img = ImageTk.PhotoImage(image=im)
    lblOutputImage.configure(image=img)
   
    lblOutputImage.image = img

    # Nhãn HÌNH ẢNH ĐẦU RA
    lblInfo3 = Label(root, text="HÌNH ẢNH ĐẦU RA:", font="bold")
    lblInfo3.grid(column=2, row=0, padx=5, pady=5)

    # hiển thị ảnh res2
    
    lblInfo4.grid(column=3, row=0, padx=5, pady=5)
    imageRes2 = []
    if(checked.get() == 1): 
        lblInfo4.configure(text="CIE LAB")
        imageRes2 = cv2.cvtColor(image, cv2.COLOR_RGB2LAB)
    if(checked.get() == 2): 
        lblInfo4.configure(text="HSV")
        imageRes2 = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
    
    
    imRes2 = Image.fromarray(imageRes2)
    imageRes2 = ImageTk.PhotoImage(image=imRes2)
    lblImageRes2.configure(image=imageRes2)
    lblImageRes2.image = imageRes2
# Tạo cửa sổ chính
root = Tk()
# Nhãn nơi hình ảnh đầu vào sẽ được hiển thị
lblInputImage = Label(root)
lblInputImage.grid(column=1, row=1, rowspan=8)

# Nhãn nơi hình ảnh đầu ra sẽ được hiển thị
lblOutputImage = Label(root)
lblOutputImage.grid(column=2, row=1, rowspan=8)

# hinh ảnh đầu ra 2
lblInfo4 = Label(root, font="bold")
lblImageRes2 = Label(root)
lblImageRes2.grid(column=3, row=1, rowspan=8)
# Nhãn Bạn muốn tô sáng màu gì?
lblInfo2 = Label(root, text="Bạn muốn tô sáng màu gì", width=25)
lblInfo2.grid(column=0, row=1, padx=5, pady=2)
# tạo các nút radio và vị trí chúng sẽ chiếm
selected = IntVar()
rad1 = Radiobutton(root, text='Màu đỏ', width=25,value=1, variable=selected, command= deteccion_color)
rad2 = Radiobutton(root, text='Màu vàng',width=25, value=2, variable=selected, command= deteccion_color)
rad3 = Radiobutton(root, text='Màu xanh da trời',width=25, value=3, variable=selected, command= deteccion_color)
rad4 = Radiobutton(root, text='Màu xanh lá cây',width=25, value=4, variable=selected, command= deteccion_color)
rad5 = Radiobutton(root, text='Màu da cam',width=25, value=5, variable=selected, command= deteccion_color)
rad6 = Radiobutton(root, text='Màu tím',width=25, value=6, variable=selected, command= deteccion_color)


rad1.grid(column=0, row=2)
rad2.grid(column=0, row=3)
rad3.grid(column=0, row=4)
rad4.grid(column=0, row=5)
rad5.grid(column=0, row=6)   
rad6.grid(column=0, row=7)

checked = IntVar()
check1 = Checkbutton(root, text="CIE LAB", width=25, onvalue=1, variable=checked,command= deteccion_color)
check2 = Checkbutton(root, text="HSV", width=25, onvalue=2, variable=checked,command= deteccion_color)
check1.grid(column=0, row=8)
check2.grid(column=0, row=9)


# Tạo nút để chọn hình ảnh đầu vào
btn = Button(root, text="chọn hình ảnh", width=25, command=choose_image)
btn.grid(column=0, row=0, padx=5, pady=5)

root.mainloop()