# snippet that extracts the company name of a given email address.

def extract_name(string):
	#find index number of '@' and '.'
	at_count=string.find("@")
	dot_count=string.find(".")

	#slice the string to get domain name
	s2=slice(at_count+1,dot_count)
	print("Your company name is : "+string[s2])
	

if __name__ == '__main__':
	# take input from user
	string=input("Enter your email : ")
	extract_name(string)
