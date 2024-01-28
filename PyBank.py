import os
import csv

# Stores the file path in the Bank_File_Loc variable.
Bank_File_Loc = os.path.join("C:/Users/jclaw/Desktop/Python-Challenge/PyBank/Resources/budget_data.csv")

# Variables:
Bank_Count = 0
Net_Total = 0
Greatest_Increase = 0
Greatest_Decrease = 0
Greatest_Increase_Date = 'Date'
Greatest_Decrease_Date = 'Date'
Numbers_List = []
Date_List = []
Numbers_Change_List = [0,]
Numbers_Change = 0
Numbers_Total = 0

# Opens the budget_data.csv file, reads it, and stores the header. 
with open(Bank_File_Loc) as csvfile:
    Bank_File_Read = csv.reader(csvfile, delimiter=',')
    print(Bank_File_Read)
    csv_header = next(Bank_File_Read)

    # Loops through the rows within the budget_data.csv file and calculates the total Profit/Loss, 
        # appending the Profit/Loss for each row to the Numbers_List list and appending
        # the dates for every row into Date_List. 
    for row in Bank_File_Read:
        Net_Total += int(row[1])
        Numbers_List.append(int(row[1]))
        Date_List.append(str(row[0]))

    # Loops through Numbers_List to return the change in Profit/Loss, 
        # and the Greatest Increase and Decrease for Profit/Loss.
    for number in range(len(Numbers_List)):

        if number >= 1 and number <= (len(Numbers_List)):
            Numbers_Change = Numbers_List[number]-Numbers_List[number-1]
            Numbers_Change_List.append(Numbers_Change)
            Numbers_Total += Numbers_Change

        if Numbers_Change > Greatest_Increase:
            Greatest_Increase = Numbers_Change

        if Numbers_Change < Greatest_Decrease:
            Greatest_Decrease = Numbers_Change

    # Merges the lists for dates and Numbers_Change.
    Zip_List = zip(Date_List, Numbers_Change_List)

    # Stores the dates for the greatest increases and decreases in Profit/Loss.
    for rows in Zip_List:
        if Greatest_Increase == rows[1]:
            Greatest_Increase_Date = rows[0]
        if Greatest_Decrease == rows[1]:
            Greatest_Decrease_Date = rows[0]

# Print results out to terminal.
print('Financial Analysis')
print('-'*30)
print(f'Total Months: {len(Numbers_List)}')
print(f'Total: ${Net_Total}')
print(f'Average Change: ${round(Numbers_Total/(len(Numbers_List)-1),ndigits=2)}')
print(f'Greatest Increase in Profits: {Greatest_Increase_Date} (${Greatest_Increase})')
print(f'Greatest Decrease in Profits: {Greatest_Decrease_Date} (${Greatest_Decrease})')

# Stores the path Where we want to our output file.
Text_File_Loc = os.path.join("C:/Users/jclaw/Desktop/PyBank_Print.txt")

# Print results out to text file:
with open(Text_File_Loc, 'w') as txt:
    print("Financial Analysis", file=txt)
    print("-"*30, file=txt)
    print(f'Total Months: {len(Numbers_List)}', file=txt)
    print(f'Total: ${Net_Total}', file=txt)
    print(f'Average Change: ${round(Numbers_Total/(len(Numbers_List)-1),ndigits=2)}', file=txt)
    print(f'Greatest Increase in Profits: {Greatest_Increase_Date} (${Greatest_Increase})', file=txt)
    print(f'Greatest Decrease in Profits: {Greatest_Decrease_Date} (${Greatest_Decrease})', file=txt)