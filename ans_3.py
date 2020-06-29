#code to convert the given two list into required format

def show_format(Employee,Salary):
	#form a dictonary
	dict1={Employee[i]:Salary[i] for i in range(len(Employee))}

	#show output in required format
	print(dict1)

if __name__ == '__main__':
	#given two list as follows
	Employee = ['Amit','Manish','Mahi','Kirti','Mafin'] 
	Salary = [20000,30000,20000,40000,25000] 
	show_format(Employee,Salary)
