# print(" Enter your  Number: ")
# a= int(input(""))
# b = 4
# print("a = ", a)
# print("b = ", b)
# print ("a+b = ",a+b)

# ================================
# (Is called assignment operator: = )


# ==============================================================================================
# Tasl NO: Mark Sheet, compute=90, science=80, Maths=70, ((1)Obetained marks=?, (2)Total marks=?,
# (3)percentage=? )

# print(" Marks Sheet ")
# print("________________")
# print(" your All Subjects Number: ")
# # All Subjects Marks.
# compute = 90.5
# Science = 80
# Maths = 70
# # Total marks of all subjects.
# TotalMarks = 300
# # Print all subjects.
# print("computer=", compute, "\nScience=", Science, "\nMaths=", Maths)
# # Addition Operation
# sum = compute + Science + Maths
# # 1st Task: print marks that you taken in exam.
# print(" Obtain marks: ", sum)
# print("_______________________")
# # 2nd Task: print Total marks.
# print("Total marks: ", TotalMarks)
# # 3rd Task:  Take percentage.
# percentage = (sum / TotalMarks) * 100
# print("Total Percentage: ", percentage)
# print("_______________________________")
# # rounding the number upto 3 decimal places
# roundedNumber = round(percentage, 4) # 1st way to roundup
# print("Here percentage rounded: ", roundedNumber)

# # rounding the number upto 4 decimal places 
# print('%.3f' % percentage)# 2nd way to roundup

# # rounding the number upto 2 decimal places
# print(format(percentage,'.2f')) # 3rd way to roundup
# print("________________________")

# ==============================================================================================

print(" Marks Sheet ")
print("________________")
print(" your All Subjects Number: ")
# All Subjects Marks.
compute = int(input("Enter Computer subject marks:"))
Science = int(input("Enter Science subject marks:"))
Maths   = int(input("Enter Maths subject marks:"))
# Total marks of all subjects.
TotalMarks = 300
# Print all subjects.
print("computer=", compute, "\nScience=", Science, "\nMaths=", Maths)
# Addition Operation
sum = compute + Science + Maths
# 1st Task: print marks that you taken in exam.
print(" Obtain marks: ", sum)
print("_______________________")
# 2nd Task: print Total marks.
print("Total marks: ", TotalMarks)
# 3rd Task:  Take percentage.
percentage = (sum / TotalMarks) * 100
print("Total Percentage: ", percentage)
print("____________________________")

print(format(percentage,'.3f')) # Round off

