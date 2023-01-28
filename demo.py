# rupee to taka conversion program
'''
rupee_conversion_rate=.78
input_taka=float(input("Enter your Tk : "))
taka=rupee_conversion_rate*input_taka

print("Your converted ammount is = ",taka)
'''

# User bio data program

'''
user_name=input("Enter user name : ")
user_email=input("Enter user email id : ")
user_phone_number=input("Enter user phone number : ")

print()
print("User name is : "+user_name)
print("User email id is : "+user_email)
print("User phone number is : "+user_phone_number)'''

'''first_name="Mr. Smith"
print(first_name.capitalize())

first_name="Mr. Smith"
print(first_name.upper())'''


def summation():
    print()
    number1 = 20
    number2 = 10
    sum: int = number1 + number2
    print("Summation is = ", sum)


# summation()


def subtraction():
    number1: int = 20
    number2: int = 10
    sub: int = number1 - number2
    print("Subtraction is = ", sub)


# subtraction()


def multiplication():
    number1: int = 20
    number2: int = 10
    mul: int = number1 * number2
    print("Multiplication is = ", mul)


# multiplication()


def devidation():
    number1: float = 20
    number2: float = 10
    div: float = number1 / number2
    print("Devidation is = ", div)


# devidation()


def dhaka():
    print()
    print("Dhaka 123")
    print("Sylhet")


# dhaka()


# taka to rupee conversion program

'''def takaconversion(rupee_conversion_rate):
    input_taka=float(input("Enter your Tk : "))
    rupee=rupee_conversion_rate*input_taka

    print("Your converted ammount is = ",rupee)


takaconversion(.78)'''


# taka to rupee conversion program with argument and parameter

'''def rupeeconversion(rupee_conversion_rate):
    taka = float(input("Enter your taka : "))
    rupee = taka * rupee_conversion_rate
    print("Your converted rupee is = ", rupee)


rupeeconversion(.78)'''

def summation(number1,number2):
    print()

    sum: int = number1 + number2
    print("Summation is = ", sum)


#summation(20,10)

'''def dhaka():
    print("Dhaka123")
for i in range (5):
    print(i)
    dhaka()'''

'''for i in range (1,10):
    print(i)'''


#if else program

'''user_name=input("Enter the user name : ")
password=input("Enter the password : ")
if user_name== "Shesir Khan" and password=="9876543210" :
    print("Login Successfully")
else:
    print("Login Failed")'''

#company affiliation program

'''number=int(input("Enter Company Affiliation : "))
if number < 3:
    print("0% Bonus")
elif number <5:
    print("50% Bonus")
elif number < 8:
    print("75% Bonus")
else :
    print("100% Bonus")'''

# String formatting
'''first_name="Kevin"
last_name="peterson"
address="Dhaka"
age=30
tax=20.2
print(f"My address is : {address} and my tax is : {tax}")'''

#list slicing
'''countries=['USA','Canada','France','Germany','UK','BD','India']
powerful_countries=countries[0:4]
print(powerful_countries)'''

#list of 5 user name with input
name1=input("Enter your name")
name2=input("Enter your name")
name3=input("Enter your name")
name4=input("Enter your name")
name5=input("Enter your name")
list =[name1+name2+name3+name4+name5]
print(list)