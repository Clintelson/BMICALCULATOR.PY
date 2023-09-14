print("BMI CALCULATOR")
print("")

while True:
    try:
        sel_weight = input("Select types of Weight: [L] Pound, [K] Kilogram > ").lower()      
    except:
        print("ambot nganung di niya ni e execute")

    if sel_weight == 'k':
            try:
                weight = float(input("Enter your weight(kg) > "))
                weight_result = weight
            except:
                print("Try again")              
            else:
                print("Your weight:", weight,"kg")
                break
       
    elif sel_weight == 'l':
            try:
                weight = float(input("Enter your weight(lb) > "))
                weight_result = float(weight / 2.205)       
            except:
                print("Try again")
            else:
                 print("Your weight:", weight,"lb")
                 break
                       
while True:
    try:
        sel_height = input("Select types of Height: [C] Centimeter, [M] Meter > ").lower()
    except:
        print("")

    if sel_height == 'c':
                try:
                     height = float(input("Enter your Height(cm) > "))
                     height_result = float(height / 100)
                except:
                     print("Try again")
                else:
                     print("Your Height:", height,"cm")
                     break
    elif sel_height == 'm':
                try:
                     height = float(input("Enter your Height(m) > "))
                     height_result = height
                except:
                     print("Try again")
                else:
                     print("Your Height:", height,"m")
                     break

bmi_result = float(weight_result / (height_result * height_result))

print("BMI RESULT: >",bmi_result)

a = 18.5
c = 25.0

if bmi_result <= 18.4:
    print("Underweight")
elif bmi_result >= 40.0:
    print("Obese")
elif a <= bmi_result <= 24.9:
    print("Normal")
elif bmi_result >= c <= 39.9:
    print("Overweight")
else:
    print("Error!")