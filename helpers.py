from tkinter import *
import constants

window = Tk()
window.title(constants.TITLE)
window.geometry(constants.WINDOWSIZE)


frame = Frame(window)
frame.pack(fill=BOTH, expand=YES)
frame.pack_propagate(False)

img = PhotoImage(file=constants.IMAGE)

background = Label(
    frame,
    image=img
    )
background.place(x=0, y=0, relwidth=1, relheight=1)

button1 = Button(
    frame,
    text="Click me!",
    width=25,
    height=5,
    bg="red",
    fg="yellow",
)

greeting = Label(
    text='hello'
)

greeting.pack()
background.pack()
button1.pack()

window.mainloop()