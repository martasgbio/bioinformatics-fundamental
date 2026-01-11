#!/bin/bash
set -e

echo "Starting basic bioinformatics pipeline..."

# Create results directory if it does not exist
mkdir -p results

# Run FASTA statistics
echo "Running FASTA statistics..."
python3 scripts/fasta_stats.py data/example.fasta

# GC content sliding window
echo "Running GC content sliding window analysis..."
python3 scripts/gc_sliding_window.py data/example.fasta

# ORF finding
echo "Running ORF detection..."
python3 scripts/find_orfs_advanced.py data/example.fasta

echo "Pipeline completed successfully!"

