#Input: A known cancer-causing mutation (eg KRAS)
#Output: List of associated cpg loci
#User needs to check to make sure that mutation name appears in data matrix
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('dis')

args = parser.parse_args()

target_chromo = '12'
target_loc = 25294434
r = int(args.dis)
f_name = "HumanMethylation450_15017482_v1-2.csv"
f = open(f_name, 'r')
output_f = f"loci_dist_{r}.txt"
out = open(output_f, 'w')

j = 100
i = 0

for line in f.readlines():
    try:
        chromo = line.split(',')[14]
        loc = line.split(',')[15]
        loc = int(loc)
    except:
        continue
    if chromo == target_chromo and loc > (target_loc - r) and loc < (target_loc + r):
        out.write(f"{line.split(',')[0]}\n")
    i += 1


f.close()
out.close()
