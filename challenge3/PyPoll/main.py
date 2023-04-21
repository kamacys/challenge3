import os
import csv
csvpath = os.path.join('Resources', 'election_data.csv')

candidates=[]
all_candidates=[]
percent_list=[]
data={}
total=0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        total+=1
        all_candidates.append(row[2])
        if row[2] in candidates:
            continue
        else:
            candidates.append(row[2])
    total-=1
for i in range(1,len(candidates)):
    count=0
    for j in range(len(all_candidates)):
        if candidates[i]==all_candidates[j]:
            count+=1
    data[candidates[i]]=count
candidates.remove(candidates[0])

print("Election Results")
print("____________________________\n")
print("Total Votes: %d"%total)

for i in candidates:
    percentage=(data[i]/total)*100
    percent_list.append(percentage)
print("%s : %f(%d)"%(i,percentage,data[i]))
print("Winner",candidates[percent_list.index(max(percent_list))])

output_file = os.path.join('Analysis', 'PyPoll_output.txt')
PyPolloutput = open(output_file, "w")

line1 = "Election Results"
line2 = "______________________________"
line3 = str("Total Votes: %d"%total)
line4 = str("%s : %f(%d)"%(i,percentage,data[i]))
line5 = str("Winner",candidates[percent_list.index(max(percent_list))])

PyPolloutput.write('{}\n{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4, line5))
