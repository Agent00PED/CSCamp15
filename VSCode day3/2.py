weight=float((input("น้ำหนัก(kg): ")))
high=float(input("ส่วนสูง(m): "))

bmi=weight/(high**2)
if(bmi<18.5):
    print("ต่ำกว่าเกณฑ์")
elif(bmi<23):
    print("ปกติสมส่วน")
elif(bmi<25):
    print("น้ำหนักเกิน")
elif(bmi<30):
    print("อ้วนระดับ 1")
elif(bmi>=30):
    print("อ้วนระดับ 2")
print("BMI = ",bmi)