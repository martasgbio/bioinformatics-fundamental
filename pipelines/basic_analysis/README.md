# Basic FASTA Sequence Analysis Pipeline

This pipeline performs a basic exploratory analysis of DNA sequences in FASTA format.
It is designed as an introductory bioinformatics workflow and as part of a professional
bioinformatics portfolio.

## Pipeline Overview

The pipeline includes the following steps:

1. FASTA sequence statistics
2. GC content analysis using a sliding window
3. ORF (Open Reading Frame) detection

All outputs are saved in the results/ directory.

## Input Data

- FASTA file containing DNA sequences
- Example input file: data/example.fasta

## Analysis Steps

### 1. FASTA Statistics

Script: scripts/fasta_stats.py

Calculates:
- Sequence length
- GC percentage

Output: results/fasta_statistics.txt

### 2. GC Content Sliding Window

Script: scripts/gc_content_sliding_window.py

Generates GC content plots along each sequence.

Outputs:
- results/seq1_gc_sliding_window.png
- results/seq2_gc_sliding_window.png

### 3. ORF Detection

Script: scripts/find_orfs_advanced.py

Detects ORFs and reports the longest ORF per sequence.

Outputs:
- results/seq1_orfs.fasta
- results/seq2_orfs.fasta

## How to Run

From the root of the repository:

bash pipelines/basic_analysis/run_basic_analysis.sh

## Requirements

- Python >= 3.8
- Biopython
- Matplotlib

Install dependencies with:

pip3 install -r requirements.txt

## Notes

This pipeline is intended for educational and portfolio purposes.

## Author

Marta Sevillano  
Bioinformatics MSc Student


