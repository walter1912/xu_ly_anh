# Importing Tkinter module
from tkinter import *
# from tkinter.ttk import *
 
# Creating master Tkinter window
master = Tk()
master.geometry("175x175")
 
# Tkinter string variable
# able to store any string value
v = StringVar(master, "1")
 
# Dictionary to create multiple buttons
values = {"RadioButton 1" : "1",
          "RadioButton 2" : "2",
          "RadioButton 3" : "3",
          "RadioButton 4" : "4",
          "RadioButton 5" : "5"}
 
# Loop is used to create multiple Radiobuttons
# rather than creating each button separately
# dùng grid để đặt vị trí radio
# for (text, value) in values.items():
#     Radiobutton(master, text = text, variable = v,
#                 value = value, 
#                 background = "light blue").grid(column=0, row=int(value))

# dùng pack() để đặt vị trí radio
for (text, value) in values.items():
    Radiobutton(master, text = text, variable = v,
        value = value).pack(side = TOP, ipady = 5)
# nếu thêm cái này vào radio thì nó sẽ không hiện nút để click
#  indicator = 0,
# Infinite loop can be terminated by
# keyboard or mouse interrupt
# or by any predefined function (destroy())
mainloop()