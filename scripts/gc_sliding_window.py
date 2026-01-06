#!/usr/bin/env python3
import os
from Bio import SeqIO
import matplotlib.pyplot as plt

script_dir = os.path.dirname(os.path.abspath(__file__))
results_dir = os.path.join(script_dir, "..", "results")
os.makedirs(results_dir, exist_ok=True)


def gc_content(seq):
    """Calculate GC percentage of a DNA sequence."""
    gc = seq.count("G") + seq.count("C")
    return (gc / len(seq)) * 100 if len(seq) > 0 else 0

def sliding_window_gc(seq, window_size):
    """Calculate GC content using a sliding window."""
    positions = []
    gc_values = []

    for i in range(0, len(seq) - window_size + 1):
        window = seq[i:i + window_size]
        positions.append(i + 1)
        gc_values.append(gc_content(window))

    return positions, gc_values

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    fasta_file = os.path.join(script_dir, "../data/example.fasta")

    window_size = 5  # small window for example sequences

    for record in SeqIO.parse(fasta_file, "fasta"):
        seq = str(record.seq).upper()
        positions, gc_values = sliding_window_gc(seq, window_size)

        plt.figure()
        plt.plot(positions, gc_values)
        plt.xlabel("Position")
        plt.ylabel("GC content (%)")
        plt.title(f"GC Sliding Window - {record.id}")
        plt.tight_layout()

        output_file = output_file = os.path.join(results_dir, f"{record.id}_gc_sliding_window.png")

        plt.savefig(output_file)
        plt.close()

        print(f"{record.id}: GC plot saved as {output_file}")

