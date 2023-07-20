# A program that allows users to input monthly sales and make a graph
# Written by: Kyla Leaman
# Date written: July 20, 2024

# Import libraries
import matplotlib.pyplot as plt

print("Enter the sales for each month. For any months with no sales or future months, add 0")
janSales = int(input("Enter the sales for January: "))
febSales = int(input("Enter the sales for February: "))
marSales = int(input("Enter the sales for March: "))
aprSales = int(input("Enter the sales for April: "))
maySales = int(input("Enter the sales for May: "))
juneSales = int(input("Enter the sales for June: "))
julySales = int(input("Enter the sales for July: "))
augSales = int(input("Enter the sales for August: "))
septSales = int(input("Enter the sales for September: "))
octSales = int(input("Enter the sales for October: "))
novSales = int(input("Enter the sales for November: "))
decSales = int(input("Enter the sales for December: "))

x_axis = ["JAN", "FEB", "MAR", "APR", "MAY", "JUNE", "JULY", "AUG", "SEPT", "OCT", "NOV", "DEC"]
y_axis = [janSales, febSales, marSales, aprSales, maySales, juneSales, julySales, augSales, septSales, octSales, novSales, decSales]

plt.title("Total Monthly Sales")
plt.scatter(x_axis, y_axis, color='black', marker='x', label="Monthly Sales ($)")
plt.plot(x_axis, y_axis, color='purple', linestyle='solid')

plt.xlabel("Month")
plt.ylabel("Sales ($)")

plt.grid(False)
plt.legend()
plt.show()