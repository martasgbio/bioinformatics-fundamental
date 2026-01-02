#!/usr/bin/env python3
import os
from Bio import SeqIO

def gc_content(seq):
    gc = seq.count("G") + seq.count("C")
    return (gc / len(seq)) * 100 if len(seq) > 0 else 0

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    fasta_file = os.path.join(script_dir, "../data/example.fasta")

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

    print("FASTA statistics")
    print("----------------")
    print(f"Number of sequences: {n_sequences}")
    print(f"Min length: {min(lengths)}")
    print(f"Max length: {max(lengths)}")
    print(f"Mean length: {sum(lengths) / len(lengths):.2f}")
    print(f"Global GC content: {(total_gc / total_bases) * 100:.2f}%")

