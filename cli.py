#!/usr/bin/python3 -i

'''
# patched: 
    line 21,30 range(, rownum + 1)

'''

class f:
    buttons = [[i for i in range(j,j+4)] for j in range(0,16,4)]
    buttons[0][0]=None

parent = f()


def shiftButtons(rownum, colnum):
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
            print('Change {} to {} !'.format(i - direction, i))
            parent.buttons[i - direction][colnum] = parent.buttons[i][colnum]
        parent.buttons[rownum][colnum] = None
    else:
        print('No none')

    #debug
    print('\n'.join('\t'.join(str(i) for i in j) for j in parent.buttons))

def stat():
    print('\n'.join('\t'.join(str(i) for i in j) for j in parent.buttons))