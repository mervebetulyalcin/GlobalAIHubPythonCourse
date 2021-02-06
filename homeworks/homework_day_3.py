"""name = 'merve'
password = '12345'

Name = str(input("Please enter your name : "))
passWord = str(input("Please enter your password :"))

if name==Name and password==passWord:
    print("Enter is successfull")
else:
    print("Please check your name and password")
"""

info_dictionary = {'merve': '12345', 'erdem':'56789'}

username = input("Please enter your username :")
password = input("Please enter your password :")
try:
    if info_dictionary[username] == password:
         print("Login Successful")
    elif info_dictionary[username] != password:
         print("Login Failed")
except KeyError:
     print("Login Failed")
