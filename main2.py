# Total amount of claims for each month

# Author: Savanna Fifield        Date: 2022-11-28

import matplotlib.pyplot as plt

# Inputs
Jan = input("Enter the amount of claims for January: ")
Feb = input("Enter the amount of claims for February: ")
Mar = input("Enter the amount of claims for March: ")
Apr = input("Enter the amount of claims for April: ")
May = input("Enter the amount of claims for May: ")
Jun = input("Enter the amount of claims for June: ")
Jul = input("Enter the amount of claims for July: ")
Aug = input("Enter the amount of claims for August: ")
Sep = input("Enter the amount of claims for September: ")
Oct = input("Enter the amount of claims for October: ")
Nov = input("Enter the amount of claims for November: ")
Dec = input("Enter the amount of claims for December: ")

# Graph Creation
x_axis = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
y_axis = [Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec]

plt.title("Monthly Claims")
plt.scatter(x_axis, y_axis, color= 'darkblue', marker='x')

plt.xlabel("Months")
plt.ylabel("Amount of Claims")

plt.grid(True)

plt.show()
