marks = [35, 67, 89, 45, 90, 54, 72]
count = 0
total = 0
result =""
for num in marks:
    total = total + num
    count = count +1
average = total / count
print("total is :",total)
print("average is :",average)
print("above average marks : ")
for num in marks :
    if average < num :
        print(num)