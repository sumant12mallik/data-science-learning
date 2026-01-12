total = 0
count = 0
while True:
    number = int(input("enter a number :  "))
    if number == 0 :
        break
    if number > 0 :
        total = total + number
        count = count +1
print(total)
print("count : ",count)