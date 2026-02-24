import sys

raw_file = sys.argv[1]
trimmed_file = sys.argv[2]
output_file = sys.argv[3]


def parse_summary(file_path):
    stats = {}
    with open(file_path) as f:
        for line in f:
            if "Reads:" in line:
                stats["Reads"] = line.strip().split(":")[1].strip()
            elif "Average read length:" in line:
                stats["Avg_length"] = line.strip().split(":")[1].strip()
            elif "GC content" in line:
                stats["GC_percent"] = line.strip().split(":")[1].strip()
    return stats


raw_stats = parse_summary(raw_file)
trimmed_stats = parse_summary(trimmed_file)

with open(output_file, "w") as out:
    out.write("Metric\tRaw\tTrimmed\n")
    out.write(f"Reads\t{raw_stats['Reads']}\t{trimmed_stats['Reads']}\n")
    out.write(f"Average_read_length\t{raw_stats['Avg_length']}\t{trimmed_stats['Avg_length']}\n")
    out.write(f"GC_percent\t{raw_stats['GC_percent']}\t{trimmed_stats['GC_percent']}\n")

print("Comparison file generated:", output_file)

