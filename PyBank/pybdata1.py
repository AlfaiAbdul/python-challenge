#importing Dependencies:
import os 
import csv

#creating and empty dict called Analysi:s
Analysis1 = {}
with open('budget_data_1.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    for row in csvreader:
        #to skip the headers:         
        if row[0] == 'Date':
            continue
        Analysis1[row[0]] = int(row[1])
    #usign the date column as a key and revenue column as value
    total_sum = sum([Analysis1[key] for key in Analysis1])
    #using the length of the of rows in the dect and after skipping the header earlier 
    # #we can calculate the total # of months
    total_month = len(Analysis1)
    #to calculate the max and min we can pass some functions to lambda to shorten the line of code:
    greatest_increase_month = max(Analysis1, key=lambda key: Analysis1[key])
    greatest_decrease_month = min(Analysis1, key=lambda key: Analysis1[key])
    # calculating the average is straightforward:
    average = total_sum/total_month
    
    
    #printing the outpus: 
    print('Financial Analysis1')
    print('--------------------------------')
    print('Total Months: %d' % total_month)
    print('Total Revenue: $%d' % total_sum)
    print('Greatest Increase in Revenue: %s ($%d)' % (greatest_increase_month, Analysis1[greatest_increase_month]))
    print('Greatest Decrease in Revenue: %s ($%d)' % (greatest_decrease_month, Analysis1[greatest_decrease_month]))
    print("Average Revenue Change: " + "$" + str(average))

#exporting the results to a text file.
    with open('Anaysis1_outputs.txt', 'w') as file:
       file.write(('Total Months: %d' % total_month) + '\n')
       for key, value in Analysis1.items():
         file.write('Greatest Increase in Revenue: %s ($%d)' % (greatest_increase_month, Analysis1[greatest_increase_month]))
         file.write('Greatest Decrease in Revenue: %s ($%d)' % (greatest_decrease_month, Analysis1[greatest_decrease_month]))
       file.write("Average Revenue Change: " + "$" + str(average))