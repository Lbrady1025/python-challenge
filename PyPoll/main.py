import csv
import os

csvpath = os.path.join("Resources","election_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader,None)

    votes = []
    candidates = []
    unique_candidates = []
    candidate1_votes = []
    candidate2_votes = []
    candidate3_votes = []
    candidate4_votes = []
    for row in csvreader:
        votes.append(row[0])
        #candidates.append(row[2])
        if row[2] not in unique_candidates:
            unique_candidates.append(row[2])
        if row[2] == unique_candidates[0]:
            candidate1_votes.append(row[2])
        elif row[2] == unique_candidates[1]:
            candidate2_votes.append(row[2])
        elif row[2] == unique_candidates[2]:
            candidate3_votes.append(row[2])
        elif row[2] == unique_candidates[3]:
            candidate4_votes.append(row[2])
    
    total_votes = len(votes)
 
    candidate1 = unique_candidates[0]
    candidate2 = unique_candidates[1]
    candidate3 = unique_candidates[2]
    candidate4 = unique_candidates[3]

    candidate1_calc = len(candidate1_votes)/total_votes
    candidate1_pct = "{:.3%}".format(candidate1_calc)

    candidate2_calc = len(candidate2_votes)/total_votes
    candidate2_pct = "{:.3%}".format(candidate2_calc)

    candidate3_calc = len(candidate3_votes)/total_votes
    candidate3_pct = "{:.3%}".format(candidate3_calc)

    candidate4_calc = len(candidate4_votes)/total_votes
    candidate4_pct = "{:.3%}".format(candidate4_calc)

    results = {
        candidate1_pct:candidate1,
        candidate2_pct:candidate2,
        candidate3_pct:candidate3,
        candidate4_pct:candidate4}

    winner = max(results)
    winner_name = results.get(max(results),None)
    #print(winner_name)

    print(f"Election Results")
    print("-------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------")
    print(f"{candidate1}: {candidate1_pct} {len(candidate1_votes)}")
    print(f"{candidate2}: {candidate2_pct} {len(candidate2_votes)}")
    print(f"{candidate3}: {candidate3_pct} {len(candidate3_votes)}")
    print(f"{candidate4}: {candidate4_pct} {len(candidate4_votes)}")
    print("-------------------")
    print(f"Winner: {winner_name}")
    print("-------------------")
    
output_path = os.path.join("Analysis","results.txt")

results_txt = open(output_path, "w")

results_txt.write("Election Results\n")
results_txt.write("-------------------\n")
results_txt.write(f"Total Votes: {total_votes}\n")
results_txt.write(f"-------------------\n")
results_txt.write(f"{candidate1}: {candidate1_pct} {len(candidate1_votes)}\n")
results_txt.write(f"{candidate2}: {candidate2_pct} {len(candidate2_votes)}\n")
results_txt.write(f"{candidate3}: {candidate3_pct} {len(candidate3_votes)}")
results_txt.write(f"{candidate4}: {candidate4_pct} {len(candidate4_votes)}\n")
results_txt.write("-------------------\n")
results_txt.write(f"Winner: {winner_name}\n")
results_txt.write("-------------------\n")
results_txt.close()
