from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("400x400")

messagebox.showinfo('Message title','Message content')
messagebox.askquestion('Message title','Message askquestion')
messagebox.askyesno('Message title','Message askyesno')
messagebox.askyesnocancel('Message title','Message askyesnocancel')
messagebox.askokcancel('Message title','Message askokcancel')
messagebox.askretrycancel('Message title','Message askretrycancel')

root.mainloop()