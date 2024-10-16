import numpy as np
import matplotlib.pyplot as plt
import statistics


months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct']
income = [2700, 3100, 9100, 4500, 3800, 1900, 4200, 4800, 2400, 7800]
expenses = [1100, 2500, 3600, 4200, 1900, 3100, 3300, 7400, 5200, 3500]
savings = np.array(income) - np.array(expenses)


plt.figure(figsize=(10, 6))
plt.plot(months, income, marker='o', color='yellow', label='Income')
plt.title('Monthly Income')
plt.xlabel('Months')
plt.ylabel('Income ($)')
plt.grid()
plt.legend()
plt.show()


plt.figure(figsize=(10, 6))
plt.bar(months, savings, color='green')
plt.title('Monthly Savings')
plt.xlabel('Months')
plt.ylabel('Savings ($)')
plt.grid(axis='y')
plt.show()


import matplotlib.pyplot as plt
months = ['January', 'February', 'March', 'April', 'May']
y = [15, 40, 10, 25, 30]
plt.figure(figsize=(8, 6))
plt.pie(y, labels=months, autopct='%1.1f%%', startangle=140)
plt.axis('equal')
plt.title('Monthly Data Distribution')
plt.show()

quarters = {
    'Q1': income[0:3],
    'Q2': income[3:6],
    'Q3': income[6:9],
    'Q4': income[9:10]
}

average_income_quarters = {q: statistics.mean(income) for q, income in quarters.items()}
print("Average Income per Quarter:")
for quarter, avg_income in average_income_quarters.items():
    print(f"{quarter}: ${avg_income:.2f}")