import os
import csv

fle = open('Resources/budget_data.csv')
file = csv.DictReader(fle, delimiter=',')

#file = csv.DictReader(open('Resources/budget_data.csv'))

months = 0
total = 0
pre_rev = 0
change = 0
gchange = 0
lchange = 0
total_chg = 0

for row in file:
    months += 1
    rev = int(row['Profit/Losses'])
    total += rev
    change = rev - pre_rev
    if (pre_rev==0):
        change=0
    total_chg += change 
    if (gchange==0):
        gchange = change
    if (gchange <= change): 
        gchange = change
        gmth    = (row['Date'])
    if (lchange==0):
        lchange = change 
    if (lchange >= change):
        lchange = change
        lmth    = (row['Date'])


    pre_rev = rev


output = f'''
Financial Analysis
----------------------------
Total Months: {months}\n
Total: $ {total:,.2f}\n
Average Change: ${total_chg/(months-1):,.2f}\n
#Greatest Increase in Profits: {gmth} {gchange:,.2f}\n
#Greatest Decrease in Profits: {lmth} {lchange:,.2f}
'''    

print(output)

# no need to close file as DictReader is a parser on the CSV
fle.close()
 

# Specify the file to write to



# Open the file using "write" mode. Specify the variable to hold the contents


output_path = os.path.join("analysis", "new.txt")
#output_path = ("C/Documents/Bootcamp/GitHub Assignements/python_challenge/PyBank/Analysis/new.txt")


#f =  open("output_path", mode='w', encoding='utf-8') 
with open(output_path, 'w') as f:
  
    #f.write('Financial Analysis  again \n')
    f.write(output)
   


f.close()
    

  





