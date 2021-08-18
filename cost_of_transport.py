# calculate Cost of Transport
import csv
import argparse
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument(
    "--file",
    action="append",
    default=[],
    type=str,
)

parser.add_argument(
    "--alpha",
    type=str,
    default="alpha_3"
)
args = parser.parse_args()

file_dir = "results/cost_of_transport/"+ args.alpha +"/"
#cot = [0 for _ in range(len(args.file))]
cot = []
for i in range(len(args.file)):
    with open(file_dir + args.file[i] + ".csv") as f:
        reader = list(csv.reader(f))
        energy = 0
        distance = 0

        for j in range(1,len(reader)):
            if reader[j][0] == "end":
            # if int(float(reader[j][0])) % 999 == 0:
                cot.append(energy / distance)
                energy = 0
                distance = 0

            else:
                energy += abs(float(reader[j][0]))
                # mg=600→900に修正(脚の重さを考慮)
                distance += abs(float(reader[j][1])) * 900

        
std = np.std(cot)
ave = np.mean(cot)
print("cost of transport", cot)
print("mean", ave)
print("std", std)

name = args.file[0]


if args.full:
    with open(file_dir + "result_"+ name+ ".csv", "w") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["cost of transport"])
        w.writerow(cot)
        w.writerow(["mean", "std", "max", "min"])
        w.writerow([ave, std, max(cot), min(cot)])
else:
    with open(file_dir + "result_"+ name+"_200k"+ ".csv", "w") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["cost of transport"])
        w.writerow(cot)
        w.writerow(["mean", "std", "max", "min"])
        w.writerow([ave, std, max(cot), min(cot)])