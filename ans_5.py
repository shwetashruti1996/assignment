#snippet that resolves ancient Chinese puzzle
#We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many 
#rabbits and how many chickens do we have? 

def find_chickens(no_head,no_legs):
	for p in range(no_head+1):
		q=no_head-p
		if((2*p)+(4*q)==no_legs):
			print("Number of chicken are : ",p)
			print("Number of rabbits are : ",q)

			return p,q


if __name__ == '__main__':
	no_head=35
	no_legs=94
	chickens=find_chickens(no_head,no_legs)