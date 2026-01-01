#!/usr/bin/env python3
import os
from Bio import SeqIO
from collections import Counter

def get_kmers(seq, k):
    """Return list of k-mers from a sequence."""
    return [seq[i:i+k] for i in range(len(seq) - k + 1)]

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    fasta_file = os.path.join(script_dir, "../data/example.fasta")

    k = 3

    for record in SeqIO.parse(fasta_file, "fasta"):
        seq = str(record.seq).upper()
        kmers = get_kmers(seq, k)
        counts = Counter(kmers)

        print(f"Sequence: {record.id}")
        for kmer, count in counts.most_common():
            print(f"{kmer}: {count}")
        print("-" * 40)

