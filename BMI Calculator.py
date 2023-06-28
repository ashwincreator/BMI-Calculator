weight = float(input("Enter your weight Kg "))
height = float(input("Enter your height m "))
BMI = float(round(weight/height**2, 2))
if BMI <= 18.5:
    print("underweight")
elif (BMI >= 18.5) and (BMI <= 25):
    print("Normal Weight")
elif (BMI >= 25) and (BMI <= 30):
    print("Over weight")
elif (BMI >= 30) and (BMI <= 35):
    print("Obese")
elif (BMI >= 35):
    print("Clinically Obese")
