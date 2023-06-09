#=======================Functions=======================
# write a simple function.
def name():
    print("sultan is here!")
name() # print function data that you entered in print statment.
print("_________________________")



# # ======================================================
# # sum function of two numbeers.
# print("_______sum function______")
# def sum(num1, num2):
#     operation = num1 + num2
#     print("number one is : ", num1, 'number two is :', num2)
#     print("Total: ", operation)

# num1 = int(input("Enter your number:"))
# num2 = int(input("Enter your number:"))
# sum(num1,num2)
# # ======================================================
# # minus function of two numbeers.
# print("minus function______")
# def min(num1, num2):
#     operation = num1 - num2
#     print("number one is : ", num1, 'number two is :', num2)
#     print("Total: ", operation)

# num1 = int(input("Enter your number:"))
# num2 = int(input("Enter your number:"))
# min(num1,num2)
# # ======================================================
# # divide function of two numbeers.
# print("_______divide function______")
# def div(num1, num2):
#     operation = num1 * num2
#     print("number one is : ", num1, 'number two is :', num2)
#     print("Total: ", operation)

# num1 = int(input("Enter your number:"))
# num2 = int(input("Enter your number:"))
# div(num1,num2)
# # ======================================================
# # multipication function of two numbeers.
# print("_______multiplication function______")
# def multi(num1, num2):
#     Divide = num1 / num2
#     print("number one is : ", num1, 'number two is :', num2)
#     print("Total: ", int(Divide))

# num1 = int(input("Enter your number:"))
# num2 = int(input("Enter your number:"))
# multi(num1,num2)




# #========================================================
# # evaluate or compress the code.
# #========================================================
# # Writting function.
# def calculator():
#     num1 = int(input("Enter first number: "))
#     symbol = input("Enter symbol for operation: ")
#     num2 = int(input("Enter second number: "))
    
#     # condition for addition operation.
#     if symbol == '+' :
#         print(num1 + num2)

#     # condition for minus operation.
#     elif symbol == '-':
#         print(num1 - num2)

#     # condition for multiplication operation.
#     elif symbol == '*':
#         print(num1 * num2)

#     # condition for division operation.
#     elif symbol == '/':
#         print(int(num1 / num2))
#     else:
#         print(" using wrong operator, please try again")

# # calling to function
# calculator()
    

#========================================================
# take a list help with function.
#========================================================
# make a list:
numbers = [ 11, 33 , 333, 43 , 345, 345, 567]
letters = ['a', 'b', 'c', 'd']
# Writting a function.
def calculator():
    num1 = int(input("Enter number: "))
    
    if num1 == 1:
        list2 = numbers
        print(list2)
    elif num1 == 2:
        list2 = letters
        print(list2)

   
# calling to function
calculator()



