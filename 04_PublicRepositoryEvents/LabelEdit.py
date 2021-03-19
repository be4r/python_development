#!/usr/bin/python3

import tkinter as tk
import tkinter.font as tkf

#TODO: focus
#TODO: tab size???



class InputLabel(tk.Label):
	pos = 0
	defaultWidth = 4
	def __init__(self, *args, **kwargs):
		self.border = tk.LabelFrame()
		print(kwargs)
		if 'width' not in kwargs:
			kwargs['width'] = self.defaultWidth
		super(InputLabel, self).__init__(*args, master = self.border, **kwargs)
		self.cursor = tk.LabelFrame(self, width = 3, height=50, bg = "#ff0000")
		self.border.grid()
		self.cursor.place(x=0, y=0)
		fnt = tkf.Font(family='Monospace', weight = 'bold', size=32)
		self.configure(font = fnt)
		self.bindKeypressListener()

	def bindKeypressListener(self):
		keySize = 26 # px
		def keyPressProcess(e):
			if self.pos > 0 and e.keycode == 22: # Backspace
				self.cursor.place(x = int(self.cursor.place_info()['x']) - keySize)
				self.configure(text = self['text'][:self.pos - 1] + self['text'][self.pos:])
				self.pos -= 1
			#elif 0x21 < e.keycode < 0x7e: 
			elif e.keycode == 9: # Esc
				return
			elif self.pos > 0 and e.keycode == 113:
				self.cursor.place(x = int(self.cursor.place_info()['x']) - keySize)
				self.pos -= 1
			elif e.keycode == 119: # LeftArrow
				if self.pos < len(self['text']):
					self.configure(text = self['text'][:self.pos] + self['text'][self.pos + 1:])
			elif self.pos <= len(self['text']) and (e.char or e.keycode == 114): # char, del or RightArrow
				if e.char in ['\r', '\x08']:
					return
				if e.char == '\t' or e.keycode == 23: # haha no tabs for u :D
					e.char = ' '
					e.keycode = 65
				self.configure(text = self['text'][:self.pos] + e.char + self['text'][self.pos:])
				if self.pos < len(self['text']):
					self.pos += 1
					self.cursor.place(x = int(self.cursor.place_info()['x']) + keySize)
			if self['text'] == '':
				self.configure(width = self.defaultWidth)
			else:
				self.configure(width = 0)
		self.border.master.bind('<KeyPress>', keyPressProcess)
		def click(e):
			self.pos = (e.x + keySize // 2) // keySize
			self.cursor.place(x = self.pos * keySize)
		self.bind('<Button-1>', click)
