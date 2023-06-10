print("===========<<< Unit Conversion Program >>>==========")
print("====================================================")
print(">>> Select Your measurement operation With help of Optional numbers."
       "\n~~1.PRESS 1 FOR Measuring Length. \n~~2.PRESS 2 FOR Measuring Area." 
       "\n~~3.PRESS 3 FOR Measuring Volume. \n~~4.PRESS 4 FOR Measuring Weight."
       "\n~~5.PRESS 5 FOR Measuring Temperature.")
print("===================================================")
# <<< lists start. >>>
Measuring_Length_list = [['Meter(m) to Inches press 1., Meter(m) to Feets press 2., Meter(m) to Yard press 3., Meter(m) to miles press 4.'],
                         ['Inch (in)'],['Feet (ft)'],['Yards (yd)'],['Miles (ml)']]
Measuring_Area_list   = [[2]]
Measuring_Volume_list = [[3]]
Measuring_Weight_list = [[4]]
Measuring_Temperature_list = [[5]]
# <<< lists end. >>>

# taking input to select list.
select_measurement = int(input('enter the operation number: '))

if select_measurement == 1 or select_measurement == 2:
    #Meter(m), Inch (in), Feet (ft), Yards (yd), Miles
    # select_units = input('enter the measuring unit: ')
    index = Measuring_Length_list
    print(index[0])

    select_units = int(input('enter the measuring unit: '))
    if select_units == 1:
       #>>> meters to inches.
        meter = float(input("Enter height in meters:"))
        inch = 39.37 * meter;  
        print ("The value of ",meter," meter in Inches is:", inch); 
    elif select_units == 2:
        meter = float(input("Enter height in meters:"))
        feet = 3.281 * meter; 
        print ("The value of ",meter," meter in Inches is:", feet);




   