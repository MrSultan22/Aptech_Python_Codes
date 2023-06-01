# list=[20,40,60,80]
# here i am finding  just one perticular index value.
# print("My list Data: ",list[2])

#-------------------
# k = len(list) 
# print(k)
# print("---------------")

# for i in range(3):
#     print("list data:", list[i])

#===========================================
# list=[30,50, 40, 44]
# while True:
#     cool = input("enter data > ")
#     if cool == '#':
#         continue
#     if cool == "correct key":
#         break
#     print(cool)
# print('done')
#==================Python List/Array Methods or Functions========================
# print("-------------Append()---------------")
# # append: Add an element to the fruits list.
# fruits = ['apple', 'banana', 'cherry']
# fruits.append(input("Enter your fruits name:"))
# print(fruits)

print("-------------Append()---------------")
# take input five times and add in list help with of append method
fruits = ['apple', 'banana', 'cherry']
for fruiits in range(6):
    fruits.append(input("Enter your fruits name:"))
    print(fruits)


# print("-------------Clear()----------------")
# # Clear: Remove all elements from the fruits1 list.
# fruits1 = ['apple', 'banana', 'cherry', 'orange']
# fruits1.clear()
# print(fruits1)

# print("-------------Copy()-----------------")
# # copy:Copy the fruits list.
# fruits2 = ['apple', 'banana', 'cherry', 'orange']
# x = fruits2.copy()
# print("list 1:",fruits2)
# print("list 2:",x)

# print("-------------Count()-----------------")
# # Count: Return the number of times the value "cherry" appears in the fruits list.
# fruits3 = ['apple', 'banana', 'cherry', 'cherry']
# y = fruits3.count("cherry")
# print('this item is in your list',y,'times.')

# print("-------------Extend()-----------------")
# #extend: Add the elements of cars to the fruits list.
# fruits4 = ['apple', 'banana', 'cherry']
# vegetables = ['potatoes', 'Tomato', 'Onion']
# fruits4.extend(vegetables)
# print(fruits4)

# print("-------------Index()-----------------")
# # Index: What is the position of the value "cherry".
# fruits5 = ['apple', 'banana', 'cherry']
# z = fruits5.index("cherry")
# print("Your item index number is: ", z ," in the fruits list.")

# print("-------------Insert()-----------------")
# # Insert the value "orange" as the second element of the fruit list:
# fruits6 = ['apple', 'banana', 'cherry']
# fruits6.insert(1, "orange")
# print(fruits6)

# print("-------------pop()-----------------")
# # Removes the element at the specified position
# fruits7 = ['apple', 'banana', 'cherry']
# fruits7.pop(2)# cherry will deleted from list b/c it is on index 2
# print("list after pop is: \n",fruits7)

