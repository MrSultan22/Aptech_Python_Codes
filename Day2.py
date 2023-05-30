print(" Marks Sheet ")
print("________________")
print(" your All Subjects Number: ")
# All Subjects Marks.
computer = 90
Science = 80
Maths = 58
# Total marks of all subjects.
TotalMarks = 300
# Print all subjects.
print("computer=", computer, "\nScience=", Science, "\nMaths=", Maths)
# Addition Operation
sum = computer + Science + Maths
# 1st Task: print marks that you taken in exam.
print(" Obtain marks: ", sum)
print("_______________________")
# 2nd Task: print Total marks.
print("Total marks: ", TotalMarks)
# 3rd Task:  Take percentage.
percentage = (sum / TotalMarks) * 100
print("Total Percentage: ", percentage)
print("_______________________________")
# rounding the number upto 2 decimal places
print(format(percentage, '.2f'))  # 3rd way to roundup
print("________________________")

if percentage >= 84:
  print("A grad")
elif percentage >= 80:
  print("B grad")
elif percentage >= 70:
  print("C grad")
else:
  print("Fail")

#======================================

if computer >=60:
  print("computer: pass")
else:
  print("computer: fail")

if Science >=60:
  print("science: pass")
else:
  print("science: fail")

if Maths >=60:
  print("Maths: pass")
else:
  print("Maths: fail")
print("________________________")
#==================================
print("________________________")
if computer>=60 and Science >= 60 and Maths >= 60:
    
  print("pass")
else:
   if Maths <60:
      print("Maths:maths failed")
   else:
     if Science <60:
        print("science: failed")

#============================================
