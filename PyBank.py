import os
import csv

csv_file_path = os.path.join("Resources","budget_data.csv")
analysis_file_path = os.path.join("Analysis","PyBank_output")

with open(csv_file_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    num_of_months = 0
    net_pnl = 0
    last_month_pnl = 0
    this_month_pnl = 0
    greatest_increase_date = ""
    greatest_decrease_date = ""
    greatest_increase = 0
    greatest_decrease = 0
    average_change = 0

    # Skip the Header
    next(csvreader)

    # Loop through looking for the video
    for row in csvreader:

        last_month_pnl = this_month_pnl

        # Parse the data and store it
        date = row[0]
        this_month_pnl = int(row[1])
        
        # The total number of months included in the dataset
        num_of_months += 1

        # The net total amount of "Profit/Losses" over the entire period
        net_pnl += this_month_pnl

        # The average of the changes in "Profit/Losses" over the entire period
        # We need to gather the difference in profit/losses so that we can find the
        # greatest swings
        if num_of_months != 1:  # if this is not the first month...
            this_month_pnl_swing = this_month_pnl - last_month_pnl
            average_change += this_month_pnl_swing

            # The greatest increase in profits (date and amount) over the entire period
            if this_month_pnl_swing > greatest_increase:
                greatest_increase_date = date
                greatest_increase = this_month_pnl_swing

            # The greatest decrease in losses (date and amount) over the entire period
            if this_month_pnl_swing < greatest_decrease:
                greatest_decrease_date = date
                greatest_decrease = this_month_pnl_swing

    # For loop complete

    average_change = average_change / (num_of_months - 1)

    # Example printout:

    # Financial Analysis
    # ----------------------------
    # Total Months: 86
    # Total: $38382578
    # Average  Change: $-2315.12
    # Greatest Increase in Profits: Feb-2012 ($1926159)
    # Greatest Decrease in Profits: Sep-2013 ($-2196167)

    #print("\n Financial Analysis\n ----------------------------")
    #print(" Total Months: ", num_of_months)
    #print(" Total: ", net_pnl)
    #print(" Average Change: ", round(average_change, 2))
    #print(" Greatest Increase in Profits: " + greatest_increase_date + " (", greatest_increase, ")")
    #print(" Greatest Decrease in Profits: " + greatest_decrease_date + " (", greatest_decrease, ")")

    output  = "\n Financial Analysis\n ----------------------------"
    output += "\n Total Months: " + str(num_of_months)
    output += "\n Total: " + str(net_pnl)
    output += "\n Average Change: " + str(round(average_change, 2))
    output += "\n Greatest Increase in Profits: " + greatest_increase_date + " (" + str(greatest_increase) + ")"
    output += "\n Greatest Decrease in Profits: " + greatest_decrease_date + " (" + str(greatest_decrease) + ")"
    output += "\n"

    print(output)

with open(analysis_file_path, 'w') as writer:
    
    writer.write(output)

