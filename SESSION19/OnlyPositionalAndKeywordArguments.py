# Only accept positional arguments.
def onlyPositionalArgument(a,b,/):
    print("Sum of {} and {} is {}".format(a,b,a+b))
onlyPositionalArgument(4,5)


# Only accept keyword arguments.
def onlyKeywordArgument(*,a,b):
    print("Multiplication of {} and {} is {}".format(a,b,a*b))

onlyKeywordArgument(b=6,a=8)