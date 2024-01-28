import os
import csv

# Variables:
Ballot_ID_List = []
Candidates_List = []
Candidates_List_2 = []
County_List = []
Candidate_Votes_1 = 0
Candidate_Votes_2 = 0
Candidate_Votes_3 = 0

# Stores the csv file path under Poll_File_Loc variable. 
Py_Poll_Loc = os.path.join("C:/Users/jclaw/Desktop/Python-Challenge/PyPoll/Resources/election_data.csv")

# Opens the election_data.csv file and stores the header row. 
with open(Py_Poll_Loc) as csvfile:
    Py_Poll_Read = csv.reader(csvfile, delimiter=',')
    csvheader = next(Py_Poll_Read)

    # Separate the columns in election_data.csv into lists.
    for row in Py_Poll_Read:
        Ballot_ID_List.append(row[0])
        County_List.append(row[1])
        Candidates_List.append(row[2])

    # Returns a complete list of candidate names in Candidate_List_3.
    for Candidate in range(len(Candidates_List)):
        if Candidates_List[Candidate] != Candidates_List[Candidate-1]:
            Candidates_List_2.append(Candidates_List[Candidate])
    Candidates_List_3 = list(dict.fromkeys(Candidates_List_2))

    # Counts the total votes for each candidate.
    for Candidate in Candidates_List:
        if Candidate == Candidates_List_3[0]:
            Candidate_Votes_1 += 1
        elif Candidate == Candidates_List_3[1]:
            Candidate_Votes_2 += 1
        elif Candidate == Candidates_List_3[2]:
            Candidate_Votes_3 += 1

    # Calculates the percentage of votes each candidate won. 
    Candidate_Percent_1 = Candidate_Votes_1 / len(Candidates_List) * 100
    Candidate_Percent_2 = Candidate_Votes_2 / len(Candidates_List) * 100
    Candidate_Percent_3 = Candidate_Votes_3 / len(Candidates_List) * 100

    # Finds the winner of the election based on greatest vote count.
    if Candidate_Votes_1 > Candidate_Votes_2 and Candidate_Votes_1 > Candidate_Votes_3:
        Election_Winner = Candidates_List_3[0]
    elif Candidate_Votes_2 > Candidate_Votes_1 and Candidate_Votes_2 > Candidate_Votes_3:
        Election_Winner = Candidates_List_3[1]
    elif Candidate_Votes_3 > Candidate_Votes_1 and Candidate_Votes_3 > Candidate_Votes_2:
        Election_Winner = Candidates_List_3[2]

# Print results out to terminal.
print("Election Results")
print('-'*25)
print(f'Total Votes: {len(Candidates_List)}')
print('-'*25)
print(f'{Candidates_List_3[0]}: {round(Candidate_Percent_1,ndigits=3)}% ({Candidate_Votes_1})')
print(f'{Candidates_List_3[1]}: {round(Candidate_Percent_2,ndigits=3)}% ({Candidate_Votes_2})')
print(f'{Candidates_List_3[2]}: {round(Candidate_Percent_3,ndigits=3)}% ({Candidate_Votes_3})')
print(f'Election Winner: {Election_Winner}')
print('-'*25)

# Stores the path Where we want to our output file:
Py_Poll_Print_Loc = os.path.join("C:/Users/jclaw/Desktop/PyPoll_Print.txt")

# Prints results out to a text file.
with open(Py_Poll_Print_Loc, 'w') as txt:
    print("Election Results", file=txt)
    print('-'*25, file=txt)
    print(f'Total Votes: {len(Candidates_List)}', file=txt)
    print('-'*25, file=txt)
    print(f'{Candidates_List_3[0]}: {round(Candidate_Percent_1,ndigits=3)}% ({Candidate_Votes_1})', file=txt)
    print(f'{Candidates_List_3[1]}: {round(Candidate_Percent_2,ndigits=3)}% ({Candidate_Votes_2})', file=txt)
    print(f'{Candidates_List_3[2]}: {round(Candidate_Percent_3,ndigits=3)}% ({Candidate_Votes_3})', file=txt)
    print(f'Election Winner: {Election_Winner}', file=txt)
    print('-'*25, file=txt)
