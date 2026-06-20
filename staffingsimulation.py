import random
import  math
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

# simulation of service
def formula(employees):  
    potential_customers = np.random.binomial(n=175200, p=0.2)      # 175200 = minutes in a year, 0.2 =  probability that a customer arrives in one of those minutes  

    capacity = (employees * 5) * 365                  # number of customers that a given number of employees can serve without queues
    line = max(0, potential_customers - capacity)      # line that forms if there are more customers than employees can serve ('max(0' makes sure line can not be negative)
    if capacity > 0:
        wait_time = (line / capacity)                   
    else:                                              # if we were to simulate zero employees this would ensure code doesnt break
        wait_time = 60
 
    k = 0.05 # impatience factor
    satisfaction = 100 * math.exp(-k * wait_time)  # as wait get longer satisfaction gets lower (starts at 100 percent)
    customer_retention = math.exp(-k * wait_time)  # as wait gets longer customers leave

    actual_customers = potential_customers * customer_retention     # number of custoemrs that actually stay  to make a purchase

    revenue = actual_customers * 50                        # assuming each customer spends $50
    daily_wage = 15 * 8                                    # each employee is payed $15 per hour for a workday of 8 hours
    payroll_cost = (employees * daily_wage) * 365          # payroll cost over a year
    profit = revenue - payroll_cost                        #profit over a year
    
    return wait_time, revenue, payroll_cost, profit, satisfaction


for employees in range(1, 21):
    wait_time, revenue, payroll_cost, profit, satisfaction = formula(employees)
    print(f"{employees:<9} | {wait_time:<8.3f}mins | ${revenue:<11,} | ${payroll_cost:<11,} | ${profit:<11,}| %{satisfaction:<12}")




employees_list = [] #                           -
profits_list = [] #                              |---- metrics that will indicate success based on company goals:
satisfaction_list = [] #                        -


#monte carlo averaging:
for employees in range (1,21):
    runtimes = 10000             # simulating results for each employee 10,000 times to create more accurate data
    sum_profit = 0
    sum_satisfaction = 0

    for x in range(runtimes):
        wait_time, revenue, payroll_cost, profit,satisfaction = formula(employees)  # had to call for all 5 values or else there was a error
        sum_profit += profit
        sum_satisfaction += satisfaction

    avg_profit = sum_profit / runtimes                          # averaging the 10,000 profit results for each number of employees
    avg_satisfaction = sum_satisfaction / runtimes                       # averaging the 10,000 satisfaction results for each number of employees

    employees_list.append(employees)
    profits_list.append(avg_profit)
    satisfaction_list.append(avg_satisfaction)


plt.plot(employees_list, profits_list,)  #  employees vs profit grpah
plt.title('Employees vs Profit')
plt.xlabel("Employees")
plt.xticks(range(1,21))
plt.ylabel ('Profit')
plt.show()

plt.plot(satisfaction_list, employees_list)  # satisfaction vs employees graph
plt.title('Satisfaction vs Employees')
plt.xlabel("Satisfaction")
plt.yticks(range(1,21))
plt.ylabel ('Employees')
plt.show()

plt.plot(satisfaction_list, profits_list)  #   satisfaction vs profits graph
plt.title('Satisfaciton vs Profit')
plt.xlabel("Satisfaciton")
plt.ylabel ('Profit')
plt.show()

best_index = profits_list.index(max(profits_list))  #               -
best_employees = employees_list[best_index]    #                     | ---  Finding what number of employees yields the best profit
best_profit = profits_list[best_index]#                             -

print("-" * 30)
print(f"OPTIMAL STAFFING LEVEL: {best_employees} employees")
print(f"PROFIT: ${best_profit:,.2f}")
print("-" * 30)
