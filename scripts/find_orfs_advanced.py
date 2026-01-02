#!/usr/bin/env python3
import sys
from Bio import SeqIO

START_CODON = "ATG"
STOP_CODONS = ["TAA", "TAG", "TGA"]

def find_orfs(seq):
    seq = seq.upper()
    orfs = []

    for frame in range(3):
        i = frame
        while i < len(seq) - 2:
            codon = seq[i:i+3]
            if codon == START_CODON:
                for j in range(i+3, len(seq)-2, 3):
                    next_codon = seq[j:j+3]
                    if next_codon in STOP_CODONS:
                        orfs.append((i+1, j+3, j+3-i))  # start, end, length
                        i = j + 3  # salto después del stop
                        break
                else:
                    i += 3
            else:
                i += 3
    return orfs

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 find_orfs_advanced.py <fasta_file>")
        sys.exit(1)

    fasta_file = sys.argv[1]

    for record in SeqIO.parse(fasta_file, "fasta"):
        orfs = find_orfs(str(record.seq))
        print(f"{record.id}: {len(orfs)} ORFs found")
        if orfs:
            max_orf = max(orfs, key=lambda x: x[2])
            print(f"Longest ORF: Start {max_orf[0]}, End {max_orf[1]}, Length {max_orf[2]} bp")

