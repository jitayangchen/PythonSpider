# -*- coding: UTF-8 -*-
from Tkinter import *
from ttk import *
import tkMessageBox

root = Tk()

menubar = Menu(root)
for item in ['file', 'edit', 'view', 'about']:
	menubar.add_command(label = item)

root['menu'] = menubar


Label(root, text = 'Account:').grid(row = 0, sticky = W)
Entry(root).grid(row = 0, column = 1, sticky = E)

Label(root, text = 'Password:').grid(row = 1, sticky = W)
Entry(root).grid(row = 1, column = 1, sticky = E)

btn = Button(root, text = 'Login')
btn.grid(row = 2, column = 1, sticky = E)
def login(event):
	tkMessageBox.showinfo("LALALA")

btn.bind("<ButtonRelease-1>", login)

root.mainloop()