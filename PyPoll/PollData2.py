#Importing Dependencies:
import os 
import csv

# creating an empty dict. called E.Candidate:
E_Candidate = {}
with open('election_data_2.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #Skip over the header line
    next(csvreader)                                  
    for row in csvreader:
        #If the current candidate exists in E_Candidate dict:
        #  increase her/his vote count, otherwise:
        #  initialize her/his vote to 1
        if row[2] in E_Candidate:  
           E_Candidate[row[2]] += 1     
        else:                       
           E_Candidate[row[2]] = 1       
total_votes = csvreader.line_num - 1

print("Election Results")
print('-------------------------------------')
print ("Total Votes: " + str(total_votes))
print('-------------------------------------')

#in this for loop:
# using candidate name as key and vote count as value
for key, value in E_Candidate.items():                                                                              
  print (key + ": " + "{0:.1f}%".format(value/total_votes * 100) + 
         " (" + str(value) + ")")
print('-------------------------------------')
print ("Winner: " + max(E_Candidate, key=E_Candidate.get) )
print('-------------------------------------')

#exporting the results as a  text file.
with open('Election Results1.txt', 'w') as file:
  file.write("Total Votes: " + str(total_votes) + '\n')
  for key, value in E_Candidate.items():
    file.write(key + ": " + "{0:.1f}%".format(value/total_votes * 100) + " (" + str(value) + ")\n")
  file.write("Winner: " + max(E_Candidate, key=E_Candidate.get) + '\n')