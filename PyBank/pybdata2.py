#importing Dependencies:
import os 
import csv

#creating and empty dict called Analysi:s
Analysis2 = {}
with open('budget_data_2.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    for row in csvreader:
        #to skip the headers:         
        if row[0] == 'Date':
            continue
        Analysis2[row[0]] = int(row[1])
    #usign the date column as a key and revenue column as value
    total_sum = sum([Analysis2[key] for key in Analysis2])
    #using the length of the of rows in the dect and after skipping the header earlier 
    # #we can calculate the total # of months
    total_month = len(Analysis2)
    #to calculate the max and min we can pass some functions to lambda to shorten the line of code:
    greatest_increase_month = max(Analysis2, key=lambda key: Analysis2[key])
    greatest_decrease_month = min(Analysis2, key=lambda key: Analysis2[key])
    # calculating the average is straightforward:
    average = total_sum/total_month
    
    
    #printing the outpus: 
    print('Financial Analysis2')
    print('--------------------------------')
    print('Total Months: %d' % total_month)
    print('Total Revenue: $%d' % total_sum)
    print('Greatest Increase in Revenue: %s ($%d)' % (greatest_increase_month, Analysis2[greatest_increase_month]))
    print('Greatest Decrease in Revenue: %s ($%d)' % (greatest_decrease_month, Analysis2[greatest_decrease_month]))
    print("Average Revenue Change: " + "$" + str(average))

#exporting the results to a text file.
    with open('Anaysis2_outputs.txt', 'w') as file:
       file.write(('Total Months: %d' % total_month) + '\n')
       for key, value in Analysis2.items():
         file.write('Greatest Increase in Revenue: %s ($%d)' % (greatest_increase_month, Analysis2[greatest_increase_month]))
         file.write('Greatest Decrease in Revenue: %s ($%d)' % (greatest_decrease_month, Analysis2[greatest_decrease_month]))
       file.write("Average Revenue Change: " + "$" + str(average))