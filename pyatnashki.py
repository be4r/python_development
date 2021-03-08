#!/usr/bin/python3

import tkinter as tk
import numpy.random as perm

class Frame(tk.Frame):
    buttons = []

    def __init__(self):
        #tk.Frame.__init__(self)
        super().__init__()
        self.initButtons((4,4))

    def initButtons(self, fieldSize):
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
        self.shuffle = tk.Button(text = 'SHUFFLE!', command = self.shuffle)
        self.exit.grid(column = 0, row = 4, columnspan = 2)
        self.shuffle.grid(column = 2, row = 4, columnspan = 2)

    def shuffle(self):
        self.buttons = perm.permutation([perm.permutation(i).tolist() for i in self.buttons]).tolist()
        for r in self.buttons:
            for i in r:
                if i:
                    i.grid(row = i.grid_info()['row'], column = i.grid_info()['column'])
        

    def genShiftButtons(parent, button):
        def shiftButtons():
            rownum, colnum = button.grid_info()['row'], button.grid_info()['column']
            row = parent.buttons[rownum]
            col = [i[colnum] for i in parent.buttons]
            if None in row:
                pos = row.index(None)
                #can shift row
                direction = 1 if pos < colnum else -1
                print('none in row')
                print('moving from {} to {} in dir {}'.format(pos,colnum,direction) )
                for i in range(pos + direction, colnum + direction, direction):
                    parent.buttons[rownum][i - direction] = parent.buttons[rownum][i]
                parent.buttons[rownum][colnum] = None
            elif None in col:
                pos = col.index(None)
                #can shift column
                direction = 1 if pos < rownum else -1
                print('none in col')
                print('moving from {} to {} in dir {}'.format(pos,rownum,direction) )
                for i in range(pos + direction, rownum + direction, direction):
                    parent.buttons[i - direction][colnum] = parent.buttons[i][colnum]
                parent.buttons[rownum][colnum] = None

            #debug
            print('\n'.join('\t'.join(str(i) for i in j) for j in parent.buttons))
            #render
            for rownum, r in enumerate(parent.buttons):
                for colnum, i in enumerate(r):
                    if i:
                        i.grid(row = rownum, column = colnum)

        return shiftButtons



#def __main__():
f = Frame()
f.mainloop()

#if __name__ == '__main__':
#    __main__()
