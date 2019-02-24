puzzle = []
domain = []
def findMRV():
    mindom = 10
    mrow = -1
    mcol = -1
    for i in range(9):
        for j in range(9):
            if(1 < len(domain[i][j]) < mindom and puzzle[i][j]==0):
                mindom=len(domain[i][j])
                mrow = i
                mcol = j
    if (mindom<10):
        return True, mrow, mcol
    return False, mrow, mcol
def rowcheck(row, num):
    for i in range(9):
        if(puzzle[row][i]==num):
            return True
    return False
def colcheck(col, num):
    for i in range(9):
        if(puzzle[i][col]==num):
            return True
    return False
def boxcheck(row, col, num):
    for i in range(3):
        for j in range (3):
            if(puzzle[i+row][j+col]==num):
                return True
    return False
def verify(row, col, num):
    c1=rowcheck(row, num)
    c2=colcheck(col, num)
    c3=boxcheck(row-row%3, col-col%3, num)
    return (not(c1 or c2 or c3))

def generate():
    global puzzle
    row = 0
    col = 0
    #if the puzzle has no empty cells, it is solved
    uns, row, col = findMRV()
    if not uns:
        return True
    for num in domain[row][col]:
        if(verify(row, col, num)):
            puzzle[row][col]=num
            if(generate()):
                return True
            puzzle[row][col]=0
    return False

def solve(dom):
    global puzzle
    global domain
    domain = dom
    puzzle = [[0 for i in range(9)] for j in range(9)]
    for i in range(9):
        for j in range(9):
            if(len(domain[i][j])==1):
                puzzle[i][j]=domain[i][j][0]
    generate()
    return puzzle
