def outer():
	first = int(input("Enter first number: "))
	def inner():
		second = int(input("Enter second number: "))
		print("Sum of two numbers {} and {} is: {}".format(first,second,first+second))
	inner()
outer()