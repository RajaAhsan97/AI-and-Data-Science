# voting system for candidates
# 1. Get records of three candidates and store them in list of dictionary
# 2. Print the records
# 3. Then raise votes for candidates
# 4. Finally display the votes

candidates = ['Candidate A', 'Candidate B', 'Candidate C']

candidates_records = []
for candidate in candidates:
    name = input("Enter name of candidate:")
    district = input("Enter district of candidate: ")

    candidate_record = {}
    is_exist = False
    if len(candidates_records) == 0:
        candidate_record['Name'] = name
        candidate_record['district'] = district
        candidate_record['votes'] = 0
        candidates_records.append(candidate_record)
        is_exist = True
    else:
        for c in candidates_records:
            if c['Name'] == name and c['district'] == district:
                print("Candidate already exist!!!!")
                is_exist = True
                break

    if not is_exist:
        candidate_record['Name'] = name
        candidate_record['district'] = district
        candidate_record['votes'] = 0

        candidates_records.append(candidate_record)

    print("Record Saved Successfully....")


print("Candidates Records")
for record in candidates_records:
    print("----------------------------------")
    print(f"Records {candidates_records.index(record)}")
    print(f"Name: {record['Name']}")
    print(f"District: {record['district']}")
    print(f"Votes: {record['votes']}")
    print("----------------------------------")




# Now vote
for _ in range(5):
    print(f"-------------------------------------------")
    for record in candidates_records:
        print(f"Enter {candidates_records.index(record)+1} to vote ({record['Name']} -> {record['district']}) ")



    vote = int(input("Enter corresponding number to vote your candidate: "))


    if vote >= 1 and vote <= len(candidates_records):
        selected_candidate = candidates_records[vote -1]
        selected_candidate['votes'] += 1
        print(f"Vote for candidate {selected_candidate['Name']} is recorded...")
    else:
        print("Invalid choice!!!")


# Voting result
print('Voting Results:')
for candidate in candidates_records:
    print(f"{candidate['Name']} secured {candidate['votes']} votes")
