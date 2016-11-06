# -*- coding: UTF-8 -*-
from Tkinter import *
from ttk import *
import tkMessageBox

root = Tk()
root.title("HAHAHA")
root.iconbitmap('D:\\PythonProjects\\PythonSpider\\test\\icon.ico')
# img = PhotoImage(file='icon.png')
# root.tk.call('wm', 'iconphoto', root._w, img)
# win = Toplevel(root)
# win.title("Centered!")

menubar = Menu(root)
for item in ['file', 'edit', 'view', 'about']:
	menubar.add_command(label = item)

root['menu'] = menubar


Label(root, text = 'Account:').grid(row = 0, sticky = W)
entry = Entry(root)
entry.grid(row = 0, column = 1, sticky = E)
entry.insert(0, "YOYOYO")

Label(root, text = 'Password:').grid(row = 1, sticky = W)
Entry(root).grid(row = 1, column = 1, sticky = E)

def login(event):
	# tkMessageBox.showinfo("LALALA")
	entry.delete(0, END)

btn = Button(root, text = 'Login')
btn.grid(row = 2, column = 1, sticky = E)

btn.bind("<ButtonRelease-1>", login)


root.update() # update window ,must do
curWidth = root.winfo_reqwidth() # get current width
curHeight = root.winfo_height() # get current height
scnWidth,scnHeight = root.maxsize() # get screen width and height
# now generate configuration information
tmpcnf = '%dx%d+%d+%d'%(curWidth,curHeight,
(scnWidth-curWidth)/2,(scnHeight-curHeight)/2)
root.geometry(tmpcnf)

root.mainloop()