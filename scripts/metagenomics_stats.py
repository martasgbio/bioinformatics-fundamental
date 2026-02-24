import sys
from Bio import SeqIO

fastq_file = sys.argv[1]
output_file = sys.argv[2]

read_count = 0
total_length = 0
gc_count = 0

for record in SeqIO.parse(fastq_file, "fastq"):
    seq = record.seq
    read_count += 1
    total_length += len(seq)
    gc_count += seq.count("G") + seq.count("C")

avg_length = total_length / read_count if read_count else 0
gc_percent = (gc_count / total_length) * 100 if total_length else 0

with open(output_file, "w") as out:
    out.write(f"Reads: {read_count}\n")
    out.write(f"Average read length: {avg_length:.2f}\n")
    out.write(f"GC content (%): {gc_percent:.2f}\n")

