import sys

raw_file = sys.argv[1]
trimmed_file = sys.argv[2]
output_file = sys.argv[3]


def extract_stats(file_path):
    total = None
    shannon = None

    with open(file_path) as f:
        for line in f:
            if line.startswith("Total_kmers"):
                total = line.strip().split("\t")[1]
            if line.startswith("Shannon_diversity"):
                shannon = line.strip().split("\t")[1]

    return total, shannon


raw_total, raw_shannon = extract_stats(raw_file)
trim_total, trim_shannon = extract_stats(trimmed_file)

with open(output_file, "w") as out:
    out.write("Metric\tRaw\tTrimmed\n")
    out.write(f"Total_kmers\t{raw_total}\t{trim_total}\n")
    out.write(f"Shannon_diversity\t{raw_shannon}\t{trim_shannon}\n")

print("Comparison generated:", output_file)

