# def zero_division():
# 	x= 9/0

# try:
# 	zero_division()
# except ZeroDivisionError as err:
# 	print("You cannot divide a number by 0", err)


while True:
    try:
		x = int(input("Please enter a number "))
		break
	except ValueError:
		print("Oops! That was not a valid number")
