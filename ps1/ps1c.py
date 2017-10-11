annual_salary = float(input("Enter the starting salary: "))
total_cost = 1000000
down_payment = total_cost * 0.25
months = 36
semi_annual_raise = .07
current_savings = 0
steps = 1
best_savings_rate = 0
r = 0.04

while(True):
    current_savings = 0
    monthly_salary = annual_salary / 12
    month = 0
    while(month < months):
        current_savings += current_savings * r / 12
        current_savings += monthly_salary * best_savings_rate / 10000
        month += 1
        if(month % 6 == 0):
            monthly_salary += monthly_salary * semi_annual_raise
    if(abs(down_payment - current_savings) <= 100):
        print("Best savings rate: "+str(best_savings_rate/10000))
        print("Steps in bisection search: "+str(steps-1))
        break
    if(best_savings_rate == 10000):
        print("It is not possible to pay the down payment in three years.")
        break
    if(down_payment > current_savings):
        best_savings_rate += round(10000 * (0.5 ** steps))
    else:
        best_savings_rate -= round(10000 * (0.5 ** steps))
    steps += 1