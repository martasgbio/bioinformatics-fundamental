#!/usr/bin/env python3
import os
from Bio import SeqIO

def gc_content(seq):
    """Calculate GC content percentage of a DNA sequence."""
    gc_count = seq.count("G") + seq.count("C")
    return round((gc_count / len(seq)) * 100, 2)

if __name__ == "__main__":
    # Obtener la carpeta donde está el script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Archivo FASTA relativo al script
    fasta_file = os.path.join(script_dir, "../data/example.fasta")

    for record in SeqIO.parse(fasta_file, "fasta"):
        print(f"{record.id}: {gc_content(str(record.seq))}% GC")


