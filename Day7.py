# # ==================simple dictionary syntax==========
# dic = { 111:'sultan', 112:'aadil', 113:''}
# print(dic[111])

# #==================change value=======================

# dic[111] = "Mr.Sultan"
# print(dic)

# #===================list in dict=====================
# dic1 = ( {1:"sultan", 2:"how are you"}, ["python", "java", "php"])
# print(type(dic1))

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Q1. write a program spcrit to sort (ascending and descending order) a dictionary by value?
# my_Dic = {1:'A', 2:'B', 3:'C', 4:'D', 5:'F'}
# print(my_Dic)
# you = my_Dic
# print(you)

# =====================================================================
# •2 Write a Python script to concatenate three dictionaries to create a
# new one.
A = { 1:33, 2:44, 3:55}
B = {1:'a', 2:'b'}
C = {1:'club', 2:'queen', 3:'king', 4:'spade'}
# D = (A,B)
# print(D)
# concatenate.
D = {}
for d in (A,B,C):
    D.update(d)
    print(D)





# =====================================================================
# Q3. Write a Python script to merge two Python dictionaries.
print('=====================================================================')
animals = {10:'elephants', 20:'lions', 15:'Deers'}
birds   = {3:'parrots', 5:"sparows",2:'ducks'}
zoo = ("animals ",animals,"Birds",birds)
print(zoo)


# =====================================================================
# •4 Write a Python script to create a dictionary where the keys are
# numbers between 1 and 15 (both included) and the values are
# square of keys.





# =====================================================================
# •Q5. Write a Python program to map two lists into a dictionary.





# =====================================================================
# Q7• Write a Python program to remove duplicates values from
# Dictionary.




# =====================================================================
# Q8• Write a python program to maintain information about each
# student of Bsc-II.




# =====================================================================
# Q9• Write a Python program to replace dictionary values with their
# sum.



# =====================================================================