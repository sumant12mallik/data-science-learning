def analyze_data(data):
    total = 0
    zero_count = 0
    positive_count = 0
    minimum = None
    maximum = None
    low = 0
    mid = 0
    high = 0
    insights = []

    for num in data:
        if num < 0:
            continue

        if num == 0:
            zero_count += 1

        if num > 0:
            total += num
            positive_count += 1

            if minimum is None:
                minimum = num
                maximum = num
            else:
                if num < minimum:
                    minimum = num
                if num > maximum:
                    maximum = num

            if num <= 10:
                low += 1
            elif num <= 50:
                mid += 1
            else:
                high += 1

    if positive_count > 0:
        average = total / positive_count
    else:
        average = 0

    if high > mid and high > low:
        insights.append("Data strong hai, high values dominate kar rahi hain")

    if zero_count > 0:
        insights.append("Zero values present — data cleaning required")

    if low > mid and low > high:
        insights.append("Low values zyada hain — improvement needed")

    return positive_count, average, minimum, maximum, low, mid, high, zero_count, insights


datasets = {
    "Branch_A": [10, 15, 0, 25, 40, 60, 0, 5, -3, 80],
    "Branch_B": [5, 8, 12, 18, 20, 0, 0, 30, 35, 45],
    "Branch_C": [2, 5, 7, 0, 0, 10, 15, 18, -1]
}

reports = {}

for name, data in datasets.items():
    reports[name] = analyze_data(data)
    
for branch, result in reports.items():
    positive, avg, min_v, max_v, low, mid, high, zero, insights = result

    print("\n-----------------------------")
    print(f"Report for {branch}")
    print("-----------------------------")
    print("Positive Count :", positive)
    print("Average        :", round(avg, 2))
    print("Minimum        :", min_v)
    print("Maximum        :", max_v)

    print("\nCategories:")
    print("  Low    :", low)
    print("  Mid    :", mid)
    print("  High   :", high)

    print("\nInsights:")
    if insights:
        for ins in insights:
            print(" -", ins)
    else:
        print(" - No major issues found")