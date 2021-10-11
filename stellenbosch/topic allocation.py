import csv
import itertools

prefs = {}
with open("topic preferences.csv", 'r', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        prefs[row["Name"]] = {}
        for topic in row.keys():
            if topic != "Name":
                prefs[row["Name"]][topic] = int(row[topic])

names = tuple(prefs.keys())
topics = tuple(prefs["Liam"].keys())
minScore = 8 * 8 + 1
mins = []
for options in itertools.permutations(topics):
    score = 0
    pairing = tuple(zip(names, options))
    for name, topic in pairing:
        score += prefs[name][topic]
    if score < minScore:
        minScore = score
        mins = [pairing]
    elif score == minScore:
        mins.append(pairing)

print(f"minimum score is {minScore}")
print(f"{len(mins)} optimal pairings found:")
for i, pairing in enumerate(mins):
    print(f"Pairing {i+1}:")
    for name, topic in pairing:
        print(f"    {name}\t{topic}\t{prefs[name][topic]}")
