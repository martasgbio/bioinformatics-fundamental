#!/usr/bin/env python3

# Read a FASTA file, calculate its codon sequence, and calculate the absolute and relative frequencies of each codon. Sort the codons from highest to lowest frequency.

import os
from Bio import SeqIO
from collections import Counter

def get_codons(seq):
    """Split a DNA sequence into codons (3 bases)."""
    codons = []
    # Solo contar codones completos
    for i in range(0, len(seq) - len(seq) % 3, 3):
        codons.append(seq[i:i+3])
    return codons

if __name__ == "__main__":
    # Ruta del archivo FASTA
    script_dir = os.path.dirname(os.path.abspath(__file__))
    fasta_path = os.path.join(script_dir, "../data/example.fasta")

    for record in SeqIO.parse(fasta_path, "fasta"):
        seq = str(record.seq).upper()

        codons = get_codons(seq)
        total_codons = len(codons)

        codon_counts = Counter(codons)

        print(f"Sequence ID: {record.id}")
        print(f"Total codons: {total_codons}")
        print("-" * 40)
        print(f"{'Codon':<10}{'Count':<10}{'Frequency (%)'}")
        print("-" * 40)

        for codon, count in codon_counts.most_common():
            freq = round((count / total_codons) * 100, 2)
            print(f"{codon:<10}{count:<10}{freq}")

        print("-" * 40)

