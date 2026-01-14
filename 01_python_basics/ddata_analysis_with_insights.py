def analyze_data(data):
    zero_count = 0
    positive_count = 0
    negative_count = 0
    total = 0
    minimum = None
    maximum = None
    freq = {}

    low = 0
    medium = 0
    high = 0

    insights = []

    for num in data:
        if num < 0:
            negative_count += 1
            continue

        if num == 0:
            zero_count += 1
            continue

        # positive numbers
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

        # frequency count
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

        # smart categorisation
        if num <= 10:
            low += 1
        elif num <= 50:
            medium += 1
        else:
            high += 1

    if positive_count > 0:
        average = total / positive_count
    else:
        average = 0

    total_valid = low + medium + high

    # 🔍 INSIGHT GENERATOR
    if total_valid > 0:
        if high > low and high > medium:
            insights.append("Majority data high category me hai → strong performance")

        if low > high:
            insights.append("Low values zyada hain → improvement needed")

    if zero_count > 0:
        insights.append("Zero values present → missing or inactive data possible")

    if negative_count > 0:
        insights.append("Negative values found → data cleaning required")

    return (
        zero_count,
        positive_count,
        total,
        average,
        minimum,
        maximum,
        freq,
        low,
        medium,
        high,
        insights
    )


# ------------------ RUN ------------------

data = [12, -5, 0, 7, 0, 18, -2, 25, 7, 18, 50, 3, 99, 0, -10]

(
    zero,
    positive,
    total,
    average,
    min_val,
    max_val,
    freq,
    low,
    medium,
    high,
    insights
) = analyze_data(data)

print("Zero count :", zero)
print("Positive count :", positive)
print("Total :", total)
print("Average :", average)
print("Minimum :", min_val)
print("Maximum :", max_val)
print("Frequency :", freq)
print("Low :", low)
print("Medium :", medium)
print("High :", high)

print("\nINSIGHTS:")
for insight in insights:
    print("-", insight)