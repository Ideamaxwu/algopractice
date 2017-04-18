def fun(a, b, c, d):
	print(a, b, c, d)

# Packing arguments	
def mySum(*args):
	sum = 0
	for i in range(0, len(args)):
		sum = sum + args[i]
	return sum
	
def funDict(**args):
	for key in args:
		print("%s = %s" % (key, args[key]))


my_list = [1, 2, 3, 4]
# Unpacking list into four arguments
fun(*my_list)

print(mySum(1, 2, 3, 4, 5))

funDict(name="geeks", ID="101", language="Python")

