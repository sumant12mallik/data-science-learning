marks = [25,28,90,80,10,50]
total = 0
for m in marks:
    total = total + m
average = total / len(marks)
print("average is : ",average)

print("below average marks :")

for m in marks:
   if m < average:
       print(m)