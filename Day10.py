print("===========<<< Unit Conversion Program >>>==========")
print("====================================================")
print(">>> Select Your measurement operation With help of Optional numbers."
       "\n~~1.PRESS 1 FOR Measuring Length. \n~~2.PRESS 2 FOR Measuring Area." 
       "\n~~3.PRESS 3 FOR Measuring Volume. \n~~4.PRESS 4 FOR Measuring Weight."
       "\n~~5.PRESS 5 FOR Measuring Temperature.")
print("===================================================")
#['Inch (in) to feets press 5., Inch (in) to yards press 6., Inch (in) to miles press 7.']
#  <<< lists start. >>>
Measuring_Length_list = [['Meter(m) to Inches press 1., Meter(m) to Feets press 2., Meter(m) to Yard press 3.,'],
                         ['yard (yd) to inche press 4.,  yard (yd) to feet press 5.'],
                         ['feets(ft) to inche press 6.'],
                         ['Inche to meter press 7., Inche to yards press 8. Inche to to feet press 9, '],
                         ['Feet (ft) to meter press 10., Feet (ft) to yard press 11.'],
                         ['yard (yd) to meter press 12.']]
Measuring_Area_list   = [[2]]
Measuring_Volume_list = [[3]]
Measuring_Weight_list = [[4]]
Measuring_Temperature_list = [[5]]
# <<< lists end. >>>

# taking input to select list.
select_measurement = int(input('enter the operation number: '))

if select_measurement == 1: #or select_measurement == 2:
    #Meter(m), Inch (in), Feet (ft), Yards (yd), Miles
    index = Measuring_Length_list
    print(index[0]) 
    print(index[1])
    print(index[2])
    print(index[3])
    print(index[4])
    print(index[5])
    

    select_units = int(input('enter the measuring unit: '))

# =============================Meter to inches, feets, yards==============================
    if select_units == 1:
       #>>> meters to inches.
        meter = float(input("Enter height in meters to convert meter into inch: "))
        inch = 39.37 * meter;  # 1 meter is equal = 39.37
        print ("The value of ",meter," meter in Inches is:", inch)

    elif select_units == 2:
        meter = float(input("Enter height in meters to convert meter into feet: "))
        #>>> feet = ft.
        feet = meter * 3.281; # 1 meter is equal = 3.281 feet.
        print ("The value of ",meter," meter in Inches is:", feet)

    elif select_units == 3:
        #>>> meters to Yards.
        meter = float(input(" Enter your meters to change meter into Yards: "))
        #>>> yards = yd.
        yd =  meter * 1.09361 # 1 meter is equal = 1.09361 yards. 
        print ('The value of ',meter," meter in yards is:", yd)
   
# =============================yards to inche, feets==============================
    elif select_units == 4:
        #>>> yard to inches.
        yard = float ( input("Enter your mile to convert yard to inches:"))
        inch = yard*36
        print ("The value of ",yard, " yards in inchs is:", inch)

    elif select_units == 5:
        #>>> yards to feet.
        yard = float ( input("Enter your yards to convert yards to feet:"))
        # feet = (ft)
        ft = yard*3
        print ("The value of ",yard, " meters in miles is:", ft)

# ================================feet to inche================================      
    elif select_units == 6:
        #>>> feet to inches.
        feet = float ( input("Enter your mile to convert mile to inches:"))
        inch = feet*12
        print ("The value of ",feet, " meters in miles is:", inch)

# ================================Inch to meter, yard, feet================================ 
    elif select_units == 7:
        # inch to meter.
        inch = float (input ( " Enter your inch to convert inches into meter: "))
        # meter = (m)
        meter = inch /39.37
        print ("The value of ",inch, " inches in miles is:", meter)

    elif select_units == 8:
        # inch to yard.
        inch = float (input ( " Enter your inch to convert inches into yard: "))
        # yard = (yd)
        yard = inch / 36
        print ("The value of ",inch, " inches in miles is:", yard)

    elif select_units == 9:
        # inch to feet.
        inch = float (input ( " Enter your inch to convert inches into feet: "))
        # feet = (ft)
        feet = inch / 12
        print ("The value of ",inch, " inches in miles is:", feet)
    
# ================================feet to meter, yard================================ 

    elif select_units == 10:
        # feet to meter.
        feet = float (input ( " Enter your feet to convert feet into meter: "))
        # meter = (m)
        meter = feet / 3.281
        print("The value of ",feet, " feet in miles is:", meter)
    
    elif select_units == 11:
        # feet to meter.
        feet = float (input ( " Enter your feet to convert feet into yard: "))
        # yard = (yd)
        yard = feet / 3
        print("The value of ",feet, " feet in miles is:", yard)

# ================================yard to meter================================ 
    elif select_units == 12:
        # yard to meter.
        yard = float (input ( " Enter your yard to convert yard into meter: "))
        # meter = (m)
        meter = yard / 1.09361
        print("The value of ",yard, " yard in miles is:", meter)

    else:
        print("invalid option, Try again")

# ================================ Length code is end here.================================ 






   
