def calculate_bmi(height, weight):
    print("Height ="+str(height))
    print("Weight ="+str(weight))
    Bmi = str((weight/(height*height)))
    BMI = float(Bmi)
    if BMI < 18.5:
        print("user is Under weight")
    elif BMI >=18.5 and BMI<=25.0:
        print("User is normal weight")
    else:
        print("user is overweight")

    print(str(BMI))
calculate_bmi(weight= 57,height=1.73)