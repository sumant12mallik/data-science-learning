def analyze_sales(data):
    total = 0
    zero_count = 0
    valid_count = 0
    minimum = None
    maximum = None

    low = 0
    mid = 0
    high = 0

    low_level = 10
    mid_level = 50

    insights = []

    for num in data:
        if num < 0:
            continue

        if num == 0:
            zero_count += 1
            continue

        # positive values
        valid_count += 1
        total += num

        if minimum is None:
            minimum = num
            maximum = num
        else:
            if num < minimum:
                minimum = num
            if num > maximum:
                maximum = num

        if num <= low_level:
            low += 1
        elif num <= mid_level:
            mid += 1
        else:
            high += 1

    if valid_count > 0:
        average = total / valid_count
    else:
        average = 0

    # ---- INSIGHTS (loop ke bahar, sirf ek baar) ----
    if high > mid and high > low:
        insights.append("Sales performance strong hai")

    if low > mid and low > high:
        insights.append("Low sales dominate — strategy improvement needed")

    if mid > high and mid > low:
        insights.append("Sales stable aur balanced hai")

    if zero_count > 0:
        insights.append("Zero sales days present — review required")

    return {
        "total": total,
        "average": round(average, 2),
        "minimum": minimum,
        "maximum": maximum,
        "low": low,
        "mid": mid,
        "high": high,
        "zero_count": zero_count,
        "insights": insights
    }


# ---------- MULTIPLE DATASETS ----------
datasets = {
    "Branch_A": [10, 15, 0, 25, 40, 60, 0, 5, -3, 80],
    "Branch_B": [5, 8, 12, 18, 20, 0, 0, 30, 35, 45],
    "Branch_C": [2, 5, 7, 0, 0, 10, 15, 18, -1]
}


# ---------- REPORT PRINTING ----------
for branch, data in datasets.items():
    report = analyze_sales(data)

    print("\n==============================")
    print(f"Sales Report : {branch}")
    print("==============================")

    print("Total Sales   :", report["total"])
    print("Average Sales :", report["average"])
    print("Minimum Sale  :", report["minimum"])
    print("Maximum Sale  :", report["maximum"])

    print("\nCategories:")
    print(" Low  :", report["low"])
    print(" Mid  :", report["mid"])
    print(" High :", report["high"])

    print("\nInsights:")
    if report["insights"]:
        for ins in report["insights"]:
            print(" -", ins)
    else:
        print(" - No major issues found")