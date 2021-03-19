#!/usr/bin/python3

import tkinter as tk
import tkinter.font as tkf
from inputlabel import InputLabel

class Frame(tk.Tk):
	def __init__(self):
		super().__init__()
		self.createWidgets()

	def createWidgets(self):
		self.l = InputLabel(text = 'label1')
		self.exit = tk.Button(text = 'Exit', command = self.quit)
		self.l.grid()
		self.exit.grid()
		self.grid()


f = Frame()
f.mainloop()

