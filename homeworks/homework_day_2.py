
"""
create a list and swap the second half of the
list with the first of the list and print this list on the screen
"""
halfList = [2,6,65,89,321,458,657]
halfList[:3],halfList[3:] = halfList[3:],halfList[:3]
print(halfList)


"""
ask the user to input a singel dgit integer to variable 'n' 
then, print out of all of the even numbers from 0 to n (including n)
"""
n = int(input("Please enter a number :"))
for i in range(n):
    if i%2 ==0:
     print(i)
