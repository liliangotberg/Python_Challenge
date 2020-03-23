# modules/library/package
import os
import csv

# file path to csv dataset
pybankpath_csv = os.path.join('..', 'Resources', 'budget_data_csv')

# open and read the csv dataset 
with open(pybankpath_csv) as csvfile:
    csvreader = csv.reader(pybankpath_csv, delimiter=",")
    csv_header = next(csvfile)

print(ope)

# review csv dataset 

# if dataset has a header, read the header row first - if no header, skip step
# each row of data after the header

# cast function to modify datatype as needed
# format into a list of dictionaries format
# create a loop to reiterate/run through range of date column
# create a loop to reiterate/run through range of profit/losses column
# loop - for x in range(:):  print(x)

'''
# review csv dataset and make necessary changes
# if dataset has a header, read the header row first - if no header, skip step
#cast function to modify datatype
#  format into a list of dictionaries format
# # create a loop to read through each row of data after the header

#for row in csvreader:
    
# Identify index of columns/values
#   date = str(pybank_data[0])
#   profit_losses = int(pybank_data[1]) # cast from str to int
# Define the function that returns the entire period in dataset
# def months(date):
# Assign descriptive names to values

# Questions and calculations/solution using Python functions and methods

# * The total number of months included in the dataset 
#def sum(date):
#  total_months = len(date) 
#* The net total amount of "Profit/Losses" over the entire period   
##  net_change = int(row[1]) - prev_net
##  prev_net = int(row[1])
##  net_change_list = net_change_list + [net_change]
##  month_of_change = month_of_change + [row[0]]

#* The average of the changes in "Profit/Losses" over the entire data period
## total_monthly_avg = sum(net_change_list) / len(net_change_list)

#* The greatest increase in profits (date and amount) over the entire period
    # greatest_increase = ["", 0] # net_change_list = [] 
 #       if net_change > greatest_increase[1]:
 #           greatest_increase[0] = row[0]
#          greatest_increase[1] = net_change

#* The greatest decrease in losses (date and amount) over the entire period 
    # greatest_decrease = ["", 9999999999999999999] 
         #   if net_change < greatest_decrease[1]:
             #   greatest_decrease[0] = row[0]
             #   greatest_decrease[1] = net_change


# create bank_analysis summary using f-string formatting
# when applicable, list index and spacing command (\n)
#bank_analysis = (
 #   f"\nPyBank Financial Analysis\n"
 #   f"---$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$---\n"
 #   f"Total Months: len(str(date))" # - keep in string
    
 #    {(date_column)}\n"
 #  f"Total: ${int(total_net)}\n" #cast datatype from string to integer 
#    f"Average  Change: ${net_monthly_avg:.2f}\n"
 #   f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
 #   f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# create variable to hold path for PyBank Analysis Summary in txt format
#pybank_analysis = os.path.join('PyBank_Financial_Analysis.txt')

# open the PyBank Analysis Summary results in text file
#with open(pybank_analysis, "w", newline="") as txtfile:
#  csvwriter = csv.writer(txtfile)

# Run Python file in VSC
#print(bank_analysis)
'''