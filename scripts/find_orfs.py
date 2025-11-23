#!/usr/bin/env python3

#find ORFs. Detect coding sequences that begin with the start codon ATG and end with a stop codon

import os
from Bio import SeqIO

def find_orfs(seq):
    """Return list of ORFs in the DNA sequence (start=ATG, stop codons=TAA/TAG/TGA)."""
    start_codon = "ATG"
    stop_codons = ["TAA", "TAG", "TGA"]
    orfs = []
    for frame in range(3):
        i = frame
        while i < len(seq) - 2:
            codon = seq[i:i+3]
            if codon == start_codon:
                for j in range(i+3, len(seq)-2, 3):
                    if seq[j:j+3] in stop_codons:
                        orfs.append(seq[i:j+3])
                        i = j
                        break
            i += 3
    return orfs

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    fasta_file = os.path.join(script_dir, "../data/example.fasta")

    for record in SeqIO.parse(fasta_file, "fasta"):
        orfs = find_orfs(str(record.seq))
        print(f"{record.id}: {len(orfs)} ORFs found")

