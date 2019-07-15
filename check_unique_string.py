# return unique character in a string
def unique_char(string1):
	ascii_list=[False for i in range(128)]#create ascii length list set it false 
	unique_char_list=[]
	for i in string1:
		if ascii_list[ord(i)] is False:#ord(i) returns ascii value of character
			ascii_list[ord(i)]=True #if ascii_list[ord(i)] is false then set the value
			#to true to determine further that the string contain duplicate character or not
			unique_char_list.append(i)# if the character is unique then append to these list
		else:
			return False,unique_char_list
	return True,unique_char_list
		
def main():
	string1=input()
	check_unique,unique_char_list=unique_char(string1)
	print("unique : {} , list of unique_char : {}".format(check_unique,unique_char_list))
if __name__ == '__main__':
	main()