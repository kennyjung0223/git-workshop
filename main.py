def add_two_nums(num1, num2):
	print(num1 + num2)

def subtract_two_nums(num1, num2):
	print(num1 - num2)
	
def multiply_two_nums(num1, num2):
	print(num1 * num2)

def divide_two_nums(num1, num2):
	# assume num2 is not equal to 0
	    print(num1 / num2)

def modular_two_nums(num1, num2):
	# assume num2 is not equal to 0
	    print(num1 % num2)

def square_two_nums(num1):
	# assume num1 > 0
	    print(num1 * num1)
	
def cube_two_nums(num1):
	# assume num1 > 0
	    print(num1 * num1 * num1)


if __name__ == '__main__':
	add_two_nums(6, 3)				# expected: 9
	subtract_two_nums(6, 3)				# expected: 3
	multiply_two_nums(6, 3)				# expected: 18
	divide_two_nums(6, 3)				# expected: 2
	modular_two_nums(6, 3)				# expected: 0
	square_two_nums(6)				# expected: 36
	cube_two_nums(6)				# expected: 216
