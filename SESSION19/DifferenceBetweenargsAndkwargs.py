
def argsExample(*args):
    print("Cumulative sum of all arguments is: {}".format(sum(args)))

def kwargsExample(**kwargs):
    print("Cumulative sum of all values is: {}".format(sum(kwargs.values())))

argsExample(1,2,3,4,5)
kwargsExample(a=10,b=2,c=3,d=4,e=5)