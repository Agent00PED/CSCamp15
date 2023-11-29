num = []

while True:
    number = float(input("Input :"))
    if number == 0 :
        break
    num.append(number)

total = num[0]
for i in range(1,len(num)):
    if i%2 == 1:
        total *= num[i]
    else:
        total /= num[i]

print("Total :",total)