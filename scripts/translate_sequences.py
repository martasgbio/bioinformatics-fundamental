#!/usr/bin/env python3
import os
from Bio import SeqIO
from Bio.Seq import Seq

def translate_dna(seq):
    """Translate DNA sequence trimming incomplete codons."""
    seq = seq.upper()
    seq_len = len(seq) - len(seq) % 3
    seq = seq[:seq_len]
    return Seq(seq).translate(to_stop=True)

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    fasta_file = os.path.join(script_dir, "../data/example.fasta")

    for record in SeqIO.parse(fasta_file, "fasta"):
        protein = translate_dna(str(record.seq))
        print(f">{record.id}")
        print(protein)

