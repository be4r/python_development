#!/usr/bin/python3

import tkinter as tk
import tkinter.font as tkf

#TODO: focus



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
		self.bindKeypressListener()

	def bindKeypressListener(self):
		def eventProcess(e):
			if self.pos > 0 and e.keycode == 22:
				self.cursor.place(x = int(self.cursor.place_info()['x']) - 26)
				self.configure(text = self['text'][:self.pos - 1] + self['text'][self.pos:])
				self.pos -= 1
			#elif 0x21 < e.keycode < 0x7e: 
			elif self.pos > 0 and e.keycode == 113:
				self.cursor.place(x = int(self.cursor.place_info()['x']) - 26)
				self.pos -= 1
			elif e.keycode == 119:
				if self.pos < len(self['text']):
					self.configure(text = self['text'][:self.pos] + self['text'][self.pos + 1:])
			elif self.pos <= len(self['text']) and (e.char or e.keycode == 114):
				if e.char in ['\r', '\x08']:
					return
				self.configure(text = self['text'][:self.pos] + e.char + self['text'][self.pos:])
				if self.pos < len(self['text']):
					self.pos += 1
					self.cursor.place(x = int(self.cursor.place_info()['x']) + 26)
		self.border.master.bind('<KeyPress>', eventProcess)