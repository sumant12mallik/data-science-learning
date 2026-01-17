def analyse_data(data) :
    zero_count = 0
    positive_count = 0
    negitive_count = 0
    total = 0
    minimum = None
    maximum = None
    low = 0
    mid = 0
    high = 0
    insight = []
    for num in data :
        if num < 0 :
            negitive_count += 1
            continue
        if num == 0 :
            zero_count += 1
        if num > 0 :
            total += num
            positive_count += 1
            
            if minimum is None :
                minimum = num 
                maximum = num
            if minimum > num :
                minimum = num
            if maximum < num :
                maximum = num
            if num < 10 :
                low += 1
            if num > 10 and num <= 50 :
                mid += 1
            if num > 50 :
                high += 1
                
    if high > mid and high > low :
                insight.append("data is strong")
            
    if zero_count > 0 :
                insight.append("data cleaning required")
                
    if high < mid and high < low :
                insight.append("low value jada hai  sudhar kiaa jaa sakta hai")
                
    if positive_count > 0 :
        average = total / positive_count
                   
    return (positive_count,average,minimum,maximum,low,mid,high,zero_count)
    

datasets = {
    "Branch_A": [10, 15, 0, 25, 40, 60, 0, 5, -3, 80],
    "Branch_B": [5, 8, 12, 18, 20, 0, 0, 30, 35, 45],
    "Branch_C": [2, 5, 7, 0, 0, 10, 15, 18, -1]
}
    
reports = {}

file = open("branch_report.csv", "w")
    
file.write("Branch,Positive,Average,Min,Max,Low,Mid,High,Health\n")

for name, data in datasets.items():
    reports[name] = analyse_data(data)
    
for branch, result in reports.items() :
    positive_count,average,minimum,maximum,low,mid,high,zero_count = result
    
    score = 0
    if high > mid:
        score += 2
    if zero_count == 0:
        score += 1
    if low > high:
        score -= 1

    if score >= 3:
        health = "Excellent"
    elif score >= 1:
        health = "Average"
    else:
        health = "Poor"
    
    
    file.write(f"{branch},{positive_count},{round(average,2)},{minimum},{maximum},{low},{mid},{high},{health}\n")
    
file.close()
