#!/usr/bin/python3

'''
PYATNASHKI
Implements a game PYATNASHKI using tkinter
Author: be4r at cid33@mail.ru
'''


import tkinter as tk
from tkinter import messagebox as mb
import numpy.random as perm

class Frame(tk.Frame): # pylint: disable=too-many-ancestors
    '''
    Pyatnashki game window
    '''
    buttons = []

    def __init__(self):
        'constructor'
        super().__init__()
        self.initButtons((4,4))

    def initButtons(self, fieldSize):
        '''
        Creates all buttons, draws them for the first time.
        Called in constructor.
        '''
        for i in range(fieldSize[0]):
            row = []
            for j in range(fieldSize[1]):
                #dont draw button 0
                row.append(tk.Button(text = str(i * fieldSize[0] + j), width=2, height=2))
                if (i,j) == (0,0):
                    row[j] = None
                else:
                    row[j].configure(command = self.genShiftButtons(row[j]))
                    row[j].grid(row = i, column = j)
                #add onclick here
            self.buttons.append(row)
        self.exit = tk.Button(text = 'EXIT', command = self.quit)
        self.shuffle = tk.Button(text = 'SHUFFLE!', command = self.shuffleField)
        self.exit.grid(column = 0, row = 4, columnspan = 2)
        self.shuffle.grid(column = 2, row = 4, columnspan = 2)

    def shuffleField(self):
        '''
        Shuffles all buttons in random order(obtained using numpy)
        Called on corresponding button press
        '''
        self.buttons = perm.permutation([perm.permutation(i).tolist() for i in self.buttons]).tolist() # pylint: disable=line-too-long
        ''' #this version aint working
        #TODO: Locate problem for some understanding
        for r in self.buttons:
            for i in r:
                if i:
                    i.grid(row = i.grid_info()['row'], column = i.grid_info()['column'])
        '''
        for rownum, r in enumerate(self.buttons):
            for colnum, i in enumerate(r):
                if i:
                    i.grid(row = rownum, column = colnum)
        self.checkWin()

    def checkWin(self):
        '''
        Checks if buttons are ordered in win-combination
        Called on each button shift and shuffle
        '''
        winconfig = [[['None', '1',  '2',  '3'],
                      ['4',    '5',  '6',  '7'],
                      ['8',    '9',  '10', '11'],
                      ['12',   '13', '14', '15']],
                     [['1',  '2',  '3',  '4'],
                      ['5',  '6',  '7',  '8'],
                      ['9',  '10', '11', '12'],
                      ['13', '14', '15', 'None']]]
        if [[i['text'] if i else 'None' for i in j] for j in self.buttons] in winconfig:
            mb.showinfo('Win!', 'Congratulations!\n'
                    'You won!\nNow you can either restart or keep playing!')

    def genShiftButtons(self, button):
        '''
        Creates event listener for each button press.
        Called in constructor
        '''
        def shiftButtons():
            rownum, colnum = button.grid_info()['row'], button.grid_info()['column']
            row = self.buttons[rownum]
            col = [i[colnum] for i in self.buttons]
            if None in row:
                pos = row.index(None)
                #can shift row
                direction = 1 if pos < colnum else -1
                print('none in row')
                print('moving from {} to {} in dir {}'.format(pos,colnum,direction) )
                for i in range(pos + direction, colnum + direction, direction):
                    self.buttons[rownum][i - direction] = self.buttons[rownum][i]
                self.buttons[rownum][colnum] = None
            elif None in col:
                pos = col.index(None)
                #can shift column
                direction = 1 if pos < rownum else -1
                print('none in col')
                print('moving from {} to {} in dir {}'.format(pos,rownum,direction) )
                for i in range(pos + direction, rownum + direction, direction):
                    self.buttons[i - direction][colnum] = self.buttons[i][colnum]
                self.buttons[rownum][colnum] = None

            #render
            for rownum, r in enumerate(self.buttons):
                for colnum, i in enumerate(r):
                    if i:
                        i.grid(row = rownum, column = colnum)
            self.checkWin()

        return shiftButtons


#def __main__():
f = Frame()
f.mainloop()

#if __name__ == '__main__':
#    __main__()
