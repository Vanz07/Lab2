def calculate_bmi(height, weight):
    print("Height ="+str(height))
    print("Weight ="+str(weight))
    Bmi = str((weight/(height*height)))
    BMI = float(Bmi)
    if BMI < 18.5:
        print("user is Under weight")
        return -1
    elif BMI >=18.5 and BMI<=25.0:
        print("User is normal weight")
        return 0
    else:
        print("user is overweight")
        return 1

    print(str(BMI))
calculate_bmi(weight= 57,height=1.73)