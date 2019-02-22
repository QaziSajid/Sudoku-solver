def findempty(puzzle, l):
    for row in range(9):
        for col in range(9):
            if(puzzle[row][col]==0):
                l[0]=row
                l[1]=col
                return True
    return False
    
def rowcheck(puzzle, row, num):
    for i in range(9):
        if(puzzle[row][i]==num):
            return True
    return False
def colcheck(puzzle, col, num):
    for i in range(9):
        if(puzzle[i][col]==num):
            return True
    return False
def boxcheck(puzzle, row, col, num):
    for i in range(3):
        for j in range (3):
            if(puzzle[i+row][j+col]==num):
                return True
    return False
    
def verify(puzzle, row, col, num):
    c1=rowcheck(puzzle, row, num)
    c2=colcheck(puzzle, col, num)
    c3=boxcheck(puzzle, row-row%3, col-col%3, num)
    return (not(c1 or c2 or c3))
    
def generate(puzzle):
    l=[0, 0]
    if(not findempty(puzzle, l)):
        return True
    row=l[0]
    col=l[1]
    for num in range (1, 10):
        if(verify(puzzle, row, col, num)):
            puzzle[row][col]=num
            if(generate(puzzle)):
                return True
            puzzle[row][col]=0
    return False

def solveSudoku(puzzle):
    generate(puzzle)
    return puzzle
