# This programm illustrates how to print multiplication table

numberOfTable = int(input("Please enter the number of table: "))
rangeOfTable = int(input("Please enter the range of table: "))

print("Table number is: ",numberOfTable, "'\n' and range of table is: ",rangeOfTable)

for i in range(1,rangeOfTable+1):
    print("(",numberOfTable," * ",i," = ",numberOfTable*i,")",end=",")