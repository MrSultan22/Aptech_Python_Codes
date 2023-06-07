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
my_Dic = {4:'A', 2:'B', 5:'C', 1:'D', 3:'F'}
print("original dictionary: ",my_Dic)
# it will make ascending order.
you = list(sorted(my_Dic.items()))
print("ascending order list: ", you)
# it will make descending order.
this = list(sorted(my_Dic.items(), reverse=True))
print("descending order list: ", this)

# =====================================================================
# •2 Write a Python script to concatenate three dictionaries to create a
# new one.
print('=====================================================================')
A = { 11:33, 22:44, 33:55}
B = {1:'a', 2:'b'}
C = {55:'club', 12:'queen', 23:'king', 34:'spade'}
# D = (A,B)
# print(D)
# concatenate.
D = {}
for d in(A,B,C):
    D.update(d)
print(D)

# =====================================================================
# Q3. Write a Python script to merge two Python dictionaries.
print('=====================================================================')
animals = {10:'elephants', 20:'lions', 15:'Deers'}
birds   = {3:'parrots', 5:"sparows",2:'ducks'}
zoo = dict(zip(animals,birds))
print(zoo)


# =====================================================================
# •4 Write a Python script to create a dictionary where the keys are
# numbers between 1 and 15 (both included) and the values are
# square of keys.
print('=====================================================================')

plants = {}
for i in range(1,16):
    plants[i]=i**2
print(plants)
print('==========================================')
# =====================================================================
# •Q5. Write a Python program to map two lists into a dictionary.
#
# answer is {1: 'A', 2: 'B', 3: 'C', 4: 'D'} because keys are 4 and values are 5 
# therefore giving this output.
# letters = ['A','B','C','D','E']
# numbers = [1,2,3,4]
#======================
letters = ['A','B','C','D','E']# consider as values in dictionary.
numbers = [1,2,3,4,5] # consider as keys in dictionary.
maping = dict(zip(numbers,letters))
print('map two lists into a dictionary: ', maping)
print('==========================================')



# =====================================================================
# Q7• Write a Python program to remove duplicates values from
# Dictionary.
plants = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E'}
for i in plants:
    if i in plants:
        plants.pop(i)
    else:
        plants.update(i)
    # plants[i]=i**2
print(plants)



# =====================================================================
# Q8• Write a python program to maintain information about each
# student of Bsc-II.




# =====================================================================
# Q9• Write a Python program to replace dictionary values with their
# sum.



# =====================================================================
