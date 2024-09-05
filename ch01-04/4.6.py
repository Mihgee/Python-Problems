KILOGRAMS_PER_POUND = 0.45359237
METERS_PER_INCH = 0.0254

weight = eval(input("Enter weight in pounds: "))
feet = eval(input("Enter feet: "))
inches = eval(input("Enter inches: "))

weightInKilograms = weight * KILOGRAMS_PER_POUND
totalHeightInches = feet * 12 + inches
heightInMeters = totalHeightInches * METERS_PER_INCH

bmi = weightInKilograms / (heightInMeters * heightInMeters)

print("BMI is", bmi)
if bmi < 18.5:
    print("You are Underweight")
elif bmi < 25:
    print("You are Normal")
elif bmi < 30:
    print("You are Overweight")
else:
    print("You are Obese")