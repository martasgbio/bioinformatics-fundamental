import sys
from collections import Counter
from Bio import SeqIO
import math

fastq_file = sys.argv[1]
output_file = sys.argv[2]
k = 4

kmer_counts = Counter()
total_kmers = 0

for record in SeqIO.parse(fastq_file, "fastq"):
    seq = str(record.seq).upper()
    for i in range(len(seq) - k + 1):
        kmer = seq[i:i+k]
        if "N" not in kmer:
            kmer_counts[kmer] += 1
            total_kmers += 1

# Calculate Shannon diversity
shannon = 0
for count in kmer_counts.values():
    p = count / total_kmers
    shannon -= p * math.log(p)

with open(output_file, "w") as out:
    out.write("kmer\tcount\n")
    for kmer, count in kmer_counts.most_common():
        out.write(f"{kmer}\t{count}\n")

    out.write(f"\nTotal_kmers\t{total_kmers}\n")
    out.write(f"Shannon_diversity\t{shannon}\n")

print("k-mer analysis completed:", output_file)

