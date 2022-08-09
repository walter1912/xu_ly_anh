from tkinter import *
 
 
root = Tk()
 
C = Canvas(root, bg="yellow",
           height=250, width=300)
 
line = C.create_line(108, 120,
                     320, 40,
                     fill="green")
 
arc = C.create_arc(180, 150, 80,
                   210, start=0,
                   extent=220,
                   fill="red")
 
oval = C.create_oval(80, 30, 140,
                     150,
                     fill="blue")
 
# C.pack()

root.title(  "Paint App ")
 
# specify size
root.geometry("800x600")
# define function when 
# mouse double click is enabled
def paint( event ):
    
    # Co-ordinates.
    x1, y1, x2, y2 = ( event.x - 3 ),( event.y - 3 ), ( event.x + 3 ),( event.y + 3 )
     
    # Colour
    Colour = "tomato"
     
    # specify type of display
    w.create_line( x1, y1, x2,
                  y2, fill = Colour )
 
 
# create canvas widget.
w = Canvas(root, width = 800, height = 600)
 
# call function when double
# click is enabled.
w.bind( "<B1-Motion>", paint )
 
# create label.
l = Label( root, text = "Double Click and Drag to draw." )
l.pack()
w.pack()
mainloop()