#code that generates the following pattern based on True or False conditions.
import sys
def show(num):
	for i in range(num,0,-1):
	    for j in range(num-i):
	        print(end="  ") # printing space and staying in same line
	    
	    for j in range(2*i-1):
	        print("* ",end="") # printing * and staying in same line
	    print()

def show1(num):
	k=0
	for i in range(1, num+1):
	    for space in range(1, (num-i)+1):
	        print(end="  ")# printing space and staying in same line

	    while k != (2*i-1):
	        print("* ", end="")# printing * and staying in same line
	        k = k + 1
	    print()
	    k = 0

if __name__ == '__main__':
	num=5
	condition = input("Enter condition : ")
	if(condition=='True'):
		show1(num)
	elif(condition=='False'):
		show(num)
	else:
		print("you have not entered either True or False!")
	