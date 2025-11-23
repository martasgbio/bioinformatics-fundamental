#!/usr/bin/env python3

#It takes the FASTA sequences and translates them into proteins, stopping at the first stop codon.

import os
from Bio.Seq import Seq
from Bio import SeqIO

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    fasta_file = os.path.join(script_dir, "../data/example.fasta")

    for record in SeqIO.parse(fasta_file, "fasta"):
        dna_seq = Seq(str(record.seq))
        protein_seq = dna_seq.translate(to_stop=True)
        print(f"{record.id}: {protein_seq}")

