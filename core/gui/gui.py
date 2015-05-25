# -*- coding:UTF-8 -*-
from tkinter import *
import os

def centering(win):
		"""
		This function is used for centering main window
		"""
		win.update_idletasks()
		width = win.winfo_width()
		frm_width = win.winfo_rootx() - win.winfo_x()
		win_width = width + 2 * frm_width
		height = win.winfo_height()
		titlebar_height = win.winfo_rooty() - win.winfo_y()
		win_height = height + titlebar_height + frm_width 
		x = win.winfo_screenwidth() // 2 - win_width // 2
		y = win.winfo_screenheight() // 2 - win_height // 2
		win.geometry('{}x{}+{}+{}'.format(width, height, x, y))


class Sucket:

    def __init__(self, window):
        """
        This function is used for all work, or in other words, this is the main window
        """
        self.window = window
        self.window.resizable(width=False, height=False)
        self.window.title('Sucket - Because dealing with sockets suck')
        base = Frame(self.window, bg='#2A1717')
        base.place(relx=0.01, rely=0.01,relheight=0.97, relwidth=0.98)
        chat = LabelFrame(base)
        chat.place(relx=0.01, rely=0.02,relheight=0.63, relwidth=0.98)
        text = Text(base)
        text.place(relx=0.01, rely=0.74,relheight=0.24, relwidth=0.84)
        bar = Scrollbar(base)
        bar.place(relx=0.84, rely=0.74,relheight=0.24, relwidth=0.03)
        bar.config(command=text.yview)
        text.config(yscrollcommand=bar.set)
        encrypt = Checkbutton(base, bg='#2A1717', fg='#ED0A0A', text="if this is active, enable hash text", command=None)
        encrypt.place(relx=0.01, rely=0.66, relheight=0.06, relwidth=0.49)
        send = Button(base, text='Send')
        send.place(relx=0.88, rely=0.74, relheight=0.20, relwidth=0.11)
 
def Program():
	"""
	this function is used for call all methods and construct the program
	"""
	root=Tk()
	root.geometry('460x240')
	acess=Sucket(root)
	centering(root)
	root.mainloop()
Program()
