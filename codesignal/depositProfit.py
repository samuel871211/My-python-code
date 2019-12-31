def depositProfit(deposit, rate, threshold):
    count = 0
    rate = 1 + rate/100
    while deposit*rate < threshold:
        deposit = deposit*rate
        count += 1
    return count+1
