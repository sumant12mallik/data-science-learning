data = [10, -2, 0, 15, 0, -5, 20, 30]

zero_count = 0
positive_sum = 0
positive_count = 0

minimum = None
maximum = None

for num in data:
    if num < 0:
        continue

    if num == 0:
        zero_count += 1
        continue

    # num > 0 (valid data)
    positive_sum += num
    positive_count += 1

    if minimum is None:
        minimum = num
        maximum = num
    else:
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num

if positive_count > 0:
    average = positive_sum / positive_count
else:
    average = 0

print("Zero count :", zero_count)
print("Minimum positive :", minimum)
print("Maximum positive :", maximum)
print("Average positive :", average)