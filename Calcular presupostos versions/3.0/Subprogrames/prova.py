from re import X
from struct import pack
import tkinter

ventana=tkinter.Tk()
x=tkinter.Entry(ventana)
x.pack()

def go ():
    thp = int(x.get())
    print(thp)


boton = tkinter.Button(ventana, command=go)
boton.pack()

ventana.mainloop()
