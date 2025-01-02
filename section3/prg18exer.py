#prog to calc BMI OF A PERSON

#BMI=WEIGHT/(HEIGHT*HEIGHT)


height=int(input("Enter your height in meter"))
weight=int(input("enter your weight in kilos"))

bmi=float(weight/(height*height))
print("BMI IS:",bmi)
if(bmi<=18.5):
    print("Underweight")
elif(bmi>18.5 or bmi<=24.9):
    print("normal weight")
elif(bmi>=24.9 or bmi==29.9):
    print("Overeight")
else:
    print("Obesity")    