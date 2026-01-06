#!/usr/bin/env python3
import os
import sys

def classify_snv(ref, alt):
    transitions = {("A","G"), ("G","A"), ("C","T"), ("T","C")}
    if (ref, alt) in transitions:
        return "transition"
    return "transversion"

if len(sys.argv) != 2:
    print("Usage: python3 variant_stats.py <vcf_file>")
    sys.exit(1)

vcf_file = sys.argv[1]

script_dir = os.path.dirname(os.path.abspath(__file__))
results_dir = os.path.join(script_dir, "..", "results")
os.makedirs(results_dir, exist_ok=True)

output_file = os.path.join(results_dir, "variant_summary.txt")

total = 0
transitions = 0
transversions = 0

with open(vcf_file) as vcf:
    for line in vcf:
        if line.startswith("#"):
            continue
        fields = line.strip().split()

        # Skip malformed lines
        if len(fields) < 5:
            continue

        ref = fields[3]
        alt = fields[4]


        if len(ref) == 1 and len(alt) == 1:
            total += 1
            if classify_snv(ref, alt) == "transition":
                transitions += 1
            else:
                transversions += 1

with open(output_file, "w") as out:
    out.write(f"Total SNVs: {total}\n")
    out.write(f"Transitions: {transitions}\n")
    out.write(f"Transversions: {transversions}\n")

print("Variant analysis completed")
print(f"Summary written to {output_file}")

