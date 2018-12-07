import os 
import csv

filename = os.path.join("..","Resources","election_data.csv") 

Khan = []
Correy = [] 
Li = []
OTooley = [] 
Win = []
votes = [] 
peoples = []
people = []
Voters = []
candiate = []

with open(filename, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    
    for people in peoples:
        if people not in Voters:
            Voters.append(candidate)
            
    for row in csvreader:
        people.append(row[2])
        votes.append(row[0])
        
        #if row[2] == "Khan":
            #Khan.append(row[0])
        #elif row[2] == "Correy":
            #Correy.append(row[0])
        #elif row[2] == "Li":
            #Li.append(row[0])
        #elif row[2] == "O'Tooley":
            #OTooley.append(row[0]) 

print ("Election Results")
print ("----------------------------")
print("Total Votes: " + str(len(votes)))
print ("----------------------------")
print ("Khan: " + str(Khan))
print ("Correy: "+ str(Correy))
print ("Li:" + str(Li))
print ("OTooley:" + str(OTooley))
print ("----------------------------")
print ("Winner:")


output_path  = os.path.join("..","PyPoll_output.text")
with open(output_path, 'a') as output:
    exportresults()