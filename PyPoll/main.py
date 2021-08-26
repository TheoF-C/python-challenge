import csv


def tally(data_lst):
    data_dct = {c: 0 for c in set(data_lst)}
    for i in data_lst:
        data_dct[i] += 1
    return data_dct


with open('election_data.csv', mode='r') as inp:
    next(inp)
    voter_info = [row[2] for row in csv.reader(inp)]
    inp.close()


with open('election_analysis.txt', mode='w') as out:
    out.write('Election Results\n-------------------------\n')
    out.write(f'Total Votes: {len(voter_info)}\n')
    out.write('-------------------------\n')

    vote_tally = tally(voter_info)
    candidates = [k for k, v in sorted(vote_tally.items(), reverse=True, key=lambda item: item[1])]
    for candidate in candidates:
        out.write(f'{candidate}: {round(100*vote_tally[candidate]/len(voter_info),3)}% ({vote_tally[candidate]})\n')

    out.write('-------------------------\n')
    out.write(f'Winner: {candidates[0]}\n')
    out.write('-------------------------')


with open('election_analysis.txt', mode='r') as read:
    for line in read:
        line = line.strip()
        print(line)
    read.close()

