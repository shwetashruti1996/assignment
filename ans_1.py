# program which takes 2 digits, X,Y as input and generates a 2-dimensional array.

def form_matrix(rows,columns):
	#initialize ro and co to zero
	ro,co=0,0
	s=[[ro*co for co in range(columns)]for ro in range(rows)]

	for row in range(rows):
		for col in range(columns):
			s[ro][co]=ro*co

	print(s)

if __name__ == '__main__':
	r=int(input("Enter the number of rows : "))
	c=int(input("Enter the number of columns : "))
	form_matrix(r,c)