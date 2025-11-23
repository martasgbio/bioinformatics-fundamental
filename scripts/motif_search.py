#!/usr/bin/env python3

#find a short motif in the sequences and return their positions

import os
from Bio import SeqIO

def find_motif(seq, motif):
    """Return positions (1-based) where motif occurs."""
    positions = []
    motif_len = len(motif)
    for i in range(len(seq) - motif_len + 1):
        if seq[i:i+motif_len] == motif:
            positions.append(i + 1)
    return positions

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    fasta_file = os.path.join(script_dir, "../data/example.fasta")
    motif = "CGT"

    for record in SeqIO.parse(fasta_file, "fasta"):
        positions = find_motif(str(record.seq), motif)
        print(f"{record.id}: motif '{motif}' found at positions {positions}")

