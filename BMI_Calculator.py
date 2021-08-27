height = float(input("Enter Height in foot:"))
height_in_meters = height*12/39.37
weight = int(input("Enter Weight in KG:"))
BMI = weight/pow(height_in_meters,2)
if BMI>25:
    print("overweight")
elif BMI<18:
    print("Underweight")
else:
    print("Fit")

print("BMI:-",BMI)

