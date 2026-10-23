import random
from random import *
# print("Random Module members and methods are: {}.".format(dir(r)))
print("random() is: {}".format(random()))
print("randint(1,5) is: {}".format(randint(1,5)))
print("uniform(1.2,8.7) is: {}".format(uniform   (1.2,8.7)))
print("randrange(1,20,2) is: {}".format(randrange(1,20,2)))
l1 = [1,2,3,4,5]
print("choice(l1) is: {}".format(choice(l1)))
print("sample(l1,3) is: {}".format(sample(l1,2)))
print("shuffle(l1) is: {}".format(shuffle(l1)))
print("l1 is: {}".format(l1))


