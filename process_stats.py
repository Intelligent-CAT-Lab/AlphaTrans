import csv
import argparse

parser = argparse.ArgumentParser(description='Process Stats')
parser.add_argument('--project', help='Project name')
args = parser.parse_args()

f =  open(f"{args.project}_stats.csv")
data = csv.reader(f)

stats = {}

for row in data:
    class_name = row[0].strip()
    status = row[3].strip()
    
    if not class_name in stats:
        stats[class_name] = (0, 0) # (total, success)

    stats[class_name] = (stats[class_name][0] + 1, stats[class_name][1] + (1 if status == "success" else 0))

flattened = []

for class_name, (total, success) in stats.items():
    flattened.append((class_name, success/total, total-success))

flattened.sort(key=lambda x: x[1])
print("Sorted by success rate")
print(*[(x[0], x[1]) for x in flattened], sep="\n")

print("\nSorted by number of failures")
flattened.sort(key=lambda x: x[2], reverse=True)
print(*[(x[0], x[2]) for x in flattened], sep="\n")
