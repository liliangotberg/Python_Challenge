# import the os and string module
import os

# import CSV files
import csv

# Set path to select file to load 
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

# Open the CSV
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

print(csvreader)

# List of questions to answer
Total_Months = 0
Net_Total = 0
Average_Change = 0
Greatest_Increase_in_Profits = 0
Greatest_Decrease_in_Profits = 0

# Create a new list to calculate the month with the greatest increase and decrease
Greatest_Increase = ["", 0]
Greatest_Decrease = ["", 99999999999999]

# Set up cvs header line
csv_header = next(csvreader)
print(f"CSV Header; {csv-header}")

# Set up Financial Analysis Report format
first_row = next(csv_reader)
total_months = total_months +1
net_total_profits_loss = net_total_profit_loss = int (first_row[1])
original_profit_loss = int (firstrow [1])

# Row information following header
for row in csvreader:

# Total number of months 
    total_months = total_months +1

# Net total of profit and losses 
net_total_profit_loss = net_total_profit_loss + int (row[1])

# Average change in profit and losses
net_change = int (row[1]) - orig_profit_loss

net_change_list = net_change_list + [net_change]
month_change_list = month_change_lost + (row[0])

# Condition loops of greatest increase and decrease in profits
if net_change > greatest_increase[1]:
    greatest_increase[0] = row[0]
    greatest_increase[1] = net_change

if net_change > greatest_decrease[1]:
    greatest_decrease[0] = row[0]
    greatest_decrease[1] = net_change

    original_profit_loss = int (row[1])

average_monthly_net_change = sum(net_change_list) / len (month_change_list)

print("Total Months: " + str (total_months))
print("Total Amount: $" + str (net_total_profit_loss))
print("Average Change in Profit/ Losses: $" + str (average_monthly_net_change))
print("Greatest Increase in Profit:" + str (greatest_increase[0]) + "/" + "$" = str (greatest_increase[1]))
print("Greatest Decrease in Profit:" + str (greatest_decrease[0]) + "/" + "$" = str (greatest_decrease[1]))

