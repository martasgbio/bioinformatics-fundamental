#!/usr/bin/env python3
import sys
import os
from Bio import SeqIO

def gc_content(seq):
    gc = seq.count("G") + seq.count("C")
    return (gc / len(seq)) * 100 if len(seq) > 0 else 0

def calculate_n50(lengths):
    lengths_sorted = sorted(lengths, reverse=True)
    total_length = sum(lengths_sorted)
    cumulative = 0

    for length in lengths_sorted:
        cumulative += length
        if cumulative >= total_length / 2:
            return length

def fasta_stats(fasta_file):
    lengths = []
    total_gc = 0
    total_bases = 0
    n_sequences = 0

    for record in SeqIO.parse(fasta_file, "fasta"):
        seq = str(record.seq).upper()
        length = len(seq)

        lengths.append(length)
        total_gc += seq.count("G") + seq.count("C")
        total_bases += length
        n_sequences += 1

    stats = {
        "Number of sequences": n_sequences,
        "Min length": min(lengths),
        "Max length": max(lengths),
        "Mean length": sum(lengths) / len(lengths),
        "N50": calculate_n50(lengths),
        "Global GC content (%)": (total_gc / total_bases) * 100
    }

    return stats

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 fasta_stats.py <fasta_file>")
        sys.exit(1)

    fasta_file = sys.argv[1]

    stats = fasta_stats(fasta_file)

    output_file = os.path.join("..", "results", "fasta_statistics.txt")
    with open(output_file, "w") as out:
        out.write("FASTA statistics\n")
        out.write("----------------\n")
        for key, value in stats.items():
            if isinstance(value, float):
                out.write(f"{key}: {value:.2f}\n")
            else:
                out.write(f"{key}: {value}\n")

    print(f"Statistics written to {output_file}")

