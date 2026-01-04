#!/usr/bin/env python3
import sys
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

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
                        orfs.append((i, j+3, frame))  # start, end, frame
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
            max_orf = max(orfs, key=lambda x: x[1]-x[0])
            print(f"Longest ORF: Start {max_orf[0]+1}, End {max_orf[1]}, Frame {max_orf[2]+1}, Length {max_orf[1]-max_orf[0]} bp")

            # Crear SeqRecord para cada ORF
            orf_records = []
            for idx, (start, end, frame) in enumerate(orfs, 1):
                seq = Seq(str(record.seq[start:end]))
                orf_rec = SeqRecord(
                    seq,
                    id=f"{record.id}_orf{idx}_frame{frame+1}",
                    description=f"Start {start+1} End {end} Frame {frame+1}"
                )
                orf_records.append(orf_rec)

            # Guardar en archivo FASTA
            output_file = os.path.join("..", "results", f"{record.id}_orfs.fasta")
            SeqIO.write(orf_records, output_file, "fasta")
            print(f"ORFs saved to {output_file}")

