# import sys

# try:
# 	f = open('text.txt')
# 	s = f.readline()
# 	print(s)
# 	i = int(s.strip())
# except OSError as err:
# 	print("OS error: {0}".format(err))
# except ValueError:
# 	print("Could not data into integer.")
# except:
# 	print("Unexpected error: ", sys.exc_info()[0])
# 	raise

with open('text.txt') as f:
	file_data = f.read()
	print(file_data)

f.close()