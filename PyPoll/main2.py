import os
import csv

fle = os.path.join("Resources","election_data.csv")

count = 0
cand = []
unique_candidate = []
vote_count = []
vote_percent = []


#for row in file:
with open(fle, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")   
    csv_header = next(csvreader)
    for row in csvreader: 
    
       count = count + 1
       cand.append(row[2])

    for c in set(cand):
        unique_candidate.append(c)
         
        y = cand.count(c)
        vote_count.append(y)

        z = (y/count) * 100
        vote_percent.append(z)
    
    winning_vote_count = max(vote_count)
    winner = unique_candidate[vote_count.index(winning_vote_count)]

    print("Election Results")
    print("----------------")
    print("Total Votes :" + str(count))
    print("-----------------")
    for i in range(len(unique_candidate)):
                print(unique_candidate[i] + ": " + str(vote_percent[i]) + "% (" + str(vote_count[i]) + ")")
                
    print("-----------------")
    print("Winner: " + str(winner))
    print("-----------------")


output_path = os.path.join("analysis", "new2.txt")

with open(output_path, 'w') as f:
    f.write("Election Results\n")
    f.write("----------------\n")
    f.write("Total Votes :" + str(count) + "\n")
    f.write("-----------------\n")
    for i in range(len(unique_candidate)):
        f.write(unique_candidate[i] + ": " + str(vote_percent[i]) + "% (" + str(vote_count[i])+ ")\n")
    f.write("---------------\n")
    f.write("Winner: " + str(winner) + ")\n")
    f.write("---------------\n")   
   
f.close()
