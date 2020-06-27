weight = int(input("Your Weight : <Kg>"))
height = int(input("Your Height : <Cm>"))
height = height/100
a=weight/(height*height)
print(f'Your BMI Is : {a}')
