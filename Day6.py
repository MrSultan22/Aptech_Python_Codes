#============== Set ===================
# simple set.
set1 = {1,2,3,5}
print(set)
print("--------------------------")
#======================================
# set with union 
set_A = {1,2,3,4,5}
set_B = {6,7,8,9,10}
print(set_A.union(set_B))
# untuched OR no mix, no change, just print
print(set_A,set_B)
# update a set into another set.
set_A.update(set_B)
print(set_A,set_B)# here set_A will updated with set_B like: = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

print("--------------------------")

#======================================
# set with intersection 
set_A = {1,2,3,4,5,7,8}
set_B = {6,7,8,9,10}
print(set_A.intersection(set_B))
print("--------------------------")
#======================================
# set with symmtric difference,
# this can't take common values.
set_A = {1,2,3,4,5,7,8}
set_B = {6,7,8,9,10}
print(set_A.difference_update(set_B))
print("--------------------------")

#======================================
# take input from user in an empaty set.
# c=set()
# for b in range(1,5):
#     b=input("enter any input")
#     c.add(b)
#     print(c)
# print("--------------------------")

#======================================
# Q: if i take repeated value than compoler give sms "take different value, it is already exist"?
#empty_set = set()
range_input = int(input("how many you have items that you wants to store: "))
for i in range (range_input):
    data_input = input("enter your items in set: ")
    if data_input in empty_set:
        print("yes",data_input,"is already exist.")
    else:
        empty_set.add(data_input)
    print(empty_set)
# print("--------------------------")


#======================================

