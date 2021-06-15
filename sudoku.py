SIZE = 9
#sudoku problem
#cells with value 0 are vacant cells
matrix = [
    [6,5,0,8,7,3,0,9,0],
    [0,0,3,2,5,0,0,0,8],
    [9,8,0,1,0,4,3,5,7],
    [1,0,5,0,0,0,0,0,0],
    [4,0,0,0,0,0,0,0,2],
    [0,0,0,0,0,0,5,0,3],
    [5,7,8,3,0,1,0,2,6],
    [2,0,0,0,4,8,9,0,0],
    [0,9,0,6,2,5,0,8,1]]

#function to print sudoku
def print_sudoku():
	for i in matrix:
		print(i)

#function to check if the cells are assigned or not
#if there is any unassigned cell
#then this function will change the values of row and column accordingly

def number_unassigned(row, col):
	num_unassign=0
	for i in range(0,SIZE):
		for j in range(0,SIZE):
			if matrix[i][j]==0:
				row=i
				column=j
				num_unassign=1
				a=[row, column, num_unassign]
				return a
	a=[-1,-1,num_unassign]
	return a

#function to check if we can put a value in a particular cell or not

def is_safe(n, r, c):
	#checking in row
	for i in range(0, SIZE):
		#there is a cell with same value
		if matrix[r][i]==n:
			return False
	#checking in column
	for i in range(0,SIZE):
		#there is a cell with same value
		if matrix[i][c]==n:
			return False

	#finally, we are checking for the sub-matrix. (r/3)*3 gives us the starting index of the row r. 
	#For example, if the value of ‘r’ is 2 then it is in the sub-matrix which starts from (0, 0). 
	#Similarly, we are getting the value of starting column by (c/3)*3. 
	#Thus, if a cell is (2,2), then this cell will be in a sub-matrix which starts from (0,0) and we are getting this value by (c/3)*3 and (r/3)*3. 
	#After getting the starting indices, we can easily iterate over the sub-matrix to check if the we can put the value ‘n’ in that sub-matrix or not.

	row_start=(r//3)*3
	col_start=(c//3)*3
	#checking submatrix
	for i in range(row_start, row_start+3):
		for j in range(col_start, col_start+3):
			if matrix[i][j]==n:
				return False

	return True

#function to check whether we can put a value in a particular cell or not

def solve_sudoku():
	row=0
	col=0
	#if all cells are assigned then the sudoku is already solved
	#pass by reference because number_unassigned will change the values of rows and columns
	a=number_unassigned(row, col)
	if a[2]==0:
		return True
	row=a[0]
	col=a[1]
	#number between 1 to 9
	for i in range(1, 10):
		#if we can assign i to the cell or not the cell is matrix [row][col]
		if is_safe(i, row, col):
			matrix[row][col] = i
			#backtracking
			if solve_sudoku():
				return True
			#if we cannot find the solution reassign the cell
			matrix[row][col]=0

	return False

if solve_sudoku():
	print_sudoku()
else:
	print("No solution")


















