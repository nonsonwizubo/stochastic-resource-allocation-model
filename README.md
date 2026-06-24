# Stochastic Staffing Optimization Model

A stochastic simulation built with Python to analyze a hypothetical service business. Trade-offs between profit, labor costs, wait times, and customer satisfaction were considered to make data-driven decisions to find the best staffing level.

Built as a learning project to develop my skills in python, stochastic modeling, and data analysis.

## Assumptions
| Variables | Value |
| :--- | :--- |
| **Simulated Operational Period** | 365 days |
| **Daily Operation** | 8 hours/day |
| **Labor Cost** | $15.00/hour per employee |
| **Transaction Value** | $50.00 (Fixed per customer) |

## Method
### 1. Simulating Customer Arrivals
In order to simulate the arrival of customers, it was assumed that for each minute, there was a 0.2 probability that a customer would arrive. 

This probability was simulated for 175200 minutes(time open yearly in minutes).
```python
potential_customers = np.random.binomial(n=175200, p=0.2)
```
### 2. Simulating Throughput
The model assumes a service capacity of 5 customers per employee. The script generates a queue for customers exceeding this capacity. 

This queue is used to calculate wait times.
```python capacity = (employees * 5) * 365                 
    line = max(0, potential_customers - capacity)      
    if capacity > 0:
        wait_time = (line / capacity)                   
```
### 3. Simulating Customer Satisfaction and Retention Rate
To calculate customer satisfaction and rentention, an exponential decay function was used to calculate the relationship between wait times and customer satisfaction. 

The longer a customer waited, satisfaction and retention scores would decrease exponentially.

For customer retention, this decrease represented customers who left without making a purchase.

```python
k = 0.05 
    satisfaction = 100 * math.exp(-k * wait_time)
    customer_retention = math.exp(-k * wait_time)
    actual_customers = potential_customers * customer_retention 
```
### 4. Simulating Revenue, Labor Cost, Profit
```python
    revenue = actual_customers * 50                        
    daily_wage = 15 * 8                                    
    payroll_cost = (employees * daily_wage) * 365          
    profit = revenue - payroll_cost                        
```
### 5. Monte Carlo Averaging
In order to get more accurate results, 10,000 simulations were averaged at each staffing level. 
```python
for employees in range (1,21):
    runtimes = 10000          
    sum_profit = 0
    sum_satisfaction = 0

    for x in range(runtimes):
        wait_time, revenue, payroll_cost, profit,satisfaction = formula(employees) 
        sum_profit += profit
        sum_satisfaction += satisfaction

    avg_profit = sum_profit / runtimes                        
    avg_satisfaction = sum_satisfaction / runtimes
```

## Findings
Through simulation I found that at 20 employees there was no wait time, and customer satisfaction and retention was at 100%, meaning maximum revenue had been acheived.

Adding more employees than this would be wasteful as it would result in losses due to uneeded labor cost with no marginal revenue gain.

So for the purpose of graphing, I only simulated outcomes from 1 through 20 employees.

### 1. Staffing vs. Profitability
*This graph shows the point of diminishing returns where labor costs begin to outweigh profit.*

![Staffing vs. Profitability](graphs/employees_vs_profit_graph.png)

Visually looking at the graph, it looks like beyond 6 employees, profit begins to decrease due to higer labor cost outweighing revenue.

### 2. Customer Satisfaction vs. Profitability
*This graph shows the trade-off between profit and customer satisfaction*

![Profit vs Satisfaction Trade Off](graphs/satisfaction_vs_profit_graph.png)

At the point of maximum profit, customer satisfaction is around 90%. Beyond this, the trade-off between labor cost and satisfaction scores becomes clear.

### 3. Customer Satisfaction vs Staffing Levels
*As number of employees increases, customer satisfaction increases exponentially.*

![Wait Time Analysis](graphs/satisfaction_vs_employees_graph.png)

This graph shows how higher staffing levels decrease wait times, resulting in higher satisfaction rates.

### Simulation Results Summary

| Employees | Avg Wait Time | Annual Revenue | Annual Payroll | Annual Profit | Customer Satisfaction |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 18.41 mins | $705,484 | $43,800 | $661,684 | 39.8% |
| 2 | 8.56 mins | $1,137,283 | $87,600 | $1,049,683 | 65.2% |
| 3 | 5.37 mins | $1,332,603 | $131,400 | $1,201,203 | 76.5% |
| 4 | 3.84 mins | $1,458,957 | $175,200 | $1,283,757 | 82.5% |
| 5 | 2.86 mins | $1,527,389 | $219,000 | $1,308,389 | 86.7% |
| 6 | 2.20 mins| $1,569,765 | $262,800 | $1,306,965 | 89.6% |
| 10 | 0.92 mins | $1,670,557 | $438,000 | $1,232,557 | 95.5% |
| 15 | 0.27 mins | $1,719,333 | $657,000 | $1,062,333 | 98.6% |
| 20 | 0.00 mins | $1,749,500 | $876,000 | $873,500 | 100.0% |

Through  this table, It shows max profit actually occurs at 5 employees

## Conclusion

Through visualization of the three graphs it appeared that at **6** employees, profit maximized with around **90%** satisfaction.

Although through a deeper analysis of the data using the table, I found that at for each added employee after the 5th, marginal labor cost began to outweigh marginal revenue. Meaning that the maximum profit actaully occured at **5** employees.

At **100%** Satisfaction, profit is **33%** lower than the maximum due to the excessive labor cost required to reach that final **13%** of customer satisfaction.

**So based on these findings, I would recommend staffing 5-6 employees. This balances max profit and relatively high customer satisfaction while avoiding the point of diminishing returns that occurs beynod this number of employees.**


## Python Libraries Used

NumPy - stochastic modeling, efficient computing

Matplotlib - data visualization







