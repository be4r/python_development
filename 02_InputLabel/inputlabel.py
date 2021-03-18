#!/usr/bin/python3

import tkinter as tk
import tkinter.font as tkf

#TODO: focus
#TODO: move keypress code to class
#TODO: change self.l to self, self to self.master



class InputLabel(tk.Label):
	pos = 0
	def __init__(self, *args, **kwargs):
		self.border = tk.LabelFrame()
		super(InputLabel, self).__init__(*args, master = self.border, **kwargs)
		self.cursor = tk.LabelFrame(self, width = 3, height=50, bg = "#ff0000")
		self.border.grid()
		self.cursor.place(x=0, y=0)
		fnt = tkf.Font(family='Monospace', weight = 'bold', size=32)
		self.configure(font = fnt)
		

class Frame(tk.Tk):
	def __init__(self):
		super().__init__()
		self.createWidgets()
		def f(e):
			if self.l.pos > 0 and e.keycode == 22:
				self.l.cursor.place(x = int(self.l.cursor.place_info()['x']) - 26)
				self.l.configure(text = self.l['text'][:self.l.pos - 1] + self.l['text'][self.l.pos:])
				self.l.pos -= 1
			#elif 0x21 < e.keycode < 0x7e: 
			elif self.l.pos > 0 and e.keycode == 113:
				self.l.cursor.place(x = int(self.l.cursor.place_info()['x']) - 26)
				self.l.pos -= 1
			elif self.l.pos <= len(self.l['text']) and (e.char or e.keycode == 114):
				self.l.configure(text = self.l['text'][:self.l.pos] + e.char + self.l['text'][self.l.pos:])
				if self.l.pos < len(self.l['text']):
					self.l.pos += 1
					self.l.cursor.place(x = int(self.l.cursor.place_info()['x']) + 26)
		self.bind('<KeyPress>', f)

	def createWidgets(self):
		self.l = InputLabel(text = 'label1')
		self.exit = tk.Button(text = 'Exit', command = self.quit)
		self.l.grid()
		self.exit.grid()
		self.grid()


f = Frame()
f.mainloop()
