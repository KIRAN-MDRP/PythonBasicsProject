# byte
list1 = [1,2,3,4,5]
byte1 = bytes(list1)
for currentIndex in range(len(byte1)):
    print(byte1[currentIndex], end=" ")
#byte1[0] = "Kiran"
print("\n")

# bytes array
byteArray = bytearray(list1)
for currentIndex in range(len(byteArray)):
    print(byteArray[currentIndex], end=" ")
byteArray[0] = 5
print(byteArray)



