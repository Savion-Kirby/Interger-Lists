#Savion Kirby - Integers through lists
import math
#Define the list
myList = []
#Ask for 5 integers
a, b, c, d, e = input("Enter five values, please put spaces in between: ").split()
#Append all the values
myList.append(a)
myList.append(b)
myList.append(c)
myList.append(d)
myList.append(e)
#Define sum to 0
total = 0
#Print the List
print() 
print('Your List:')
for i in myList:
    print(i, end=" ")
#Add all the values
for x in range(0,5):
    total = total + int(myList[x])
    if x == 4:
        #Adding total to the list
        total = total/5
        myList.append(total)
        print()
        #Displaying total in the list
        print('List with the mean:')
        print(myList)
#Defineing the median
median = len(myList)/2
#Remove the median of the list
myList.remove(myList[int(median)])
print('List with the median removed:')
print(myList)
#Insert the two zeros at the start of the list
myList.insert(0, 0)
myList.insert(0, 0)
#Diplaying the zeros in the list
print('List with two zeros at the begining:')
print(myList)



