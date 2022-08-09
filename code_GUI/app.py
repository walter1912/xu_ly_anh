from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox 
from tkinter.ttk import *

 
window = Tk()
 
window.title("Welcome to LikeGeeks app")
# label
lbl = Label(window, text="Hello",font=("Arial Bold", 14))
 
lbl.grid(column=0, row=0)
# tạo trường nhập văn bản
txt = Entry(window, width=20)
txt.grid(column=0, row=1)
txt.focus()
# tạo combobox
combo = Combobox(window)
combo['values'] = (1,2,3,4,5,"test", "fsdf$$%")
combo.current(6)
combo.grid(column=0, row=2)

# tạo checkbox
checkbox1 = Checkbutton(window, text="Choose1")
checkbox1.grid(column=0, row=3)
checkbox2 = Checkbutton(window, text="Choose2")
checkbox2.grid(column=1, row=3)
checkbox3 = Checkbutton(window, text="Choose3")
checkbox3.grid(column=2, row=3)

# tạo radio 
selected = IntVar()
rad1 = Radiobutton(window,text='First', value=1, variable=selected)
 
rad2 = Radiobutton(window,text='Second', value=2, variable=selected)
 
rad3 = Radiobutton(window,text='Third', value=3, variable=selected)
 
rad1.grid(column=0, row=4)
 
rad2.grid(column=1, row=4)
 
rad3.grid(column=2, row=4)

# tạo hàm khi chọn radio
def radioCheck():
    print(selected.get())

# tạo text area 
txtArea = scrolledtext.ScrolledText(window,width=40,height=10)
txtArea.grid(column=0, row=5)
# tạo hàm khi click
ktclick = True
def clicked():
    res = "txt= "+txt.get()+" ;comboBox= "+combo.get()
    lbl.configure(text=res)
    print(selected.get())
    # chèn nội dung vào text area 
    txtArea.insert(INSERT,res)
    # xóa nội dung ở text area 
    txtArea.delete(1.0, END)

# tạo 1 hộp thông báo 
def showMes(t):
    if t == 0:
        messagebox.showinfo('Message title','Message content')
    if t == 1:
        res = messagebox.askquestion('Message title','Message askquestion')
    if t == 2:
        res = messagebox.askyesno('Message title','Message askyesno')
    if t == 3:
        res = messagebox.askyesnocancel('Message title','Message askyesnocancel')
    if t == 4:
        res = messagebox.askokcancel('Message title','Message askokcancel')
    if t == 5:
        res = messagebox.askretrycancel('Message title','Message askretrycancel')
    # return res

showMes(5)

# button
btn = Button(window, text="Click Me", command=clicked )
btn.grid(column=1, row=0)

# window size
window.geometry('650x400')
window.mainloop()