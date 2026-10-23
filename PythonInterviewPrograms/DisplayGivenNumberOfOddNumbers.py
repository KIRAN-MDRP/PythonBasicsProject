# This programm illustrates how to display given Number of Odd Or Even Numbers

inputCount = int(input("Enter number of values: "))
for i in range(1,inputCount+1,2):
    print(i,end=" ")