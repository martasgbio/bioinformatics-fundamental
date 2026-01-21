# Variant Analysis Pipeline

This pipeline performs a basic analysis of genetic variants from a VCF file.
It is designed as an introductory workflow and as part of a professional
bioinformatics portfolio.

---

## Pipeline Overview

The pipeline includes the following steps:

1. Parsing a VCF file
2. Computing basic variant statistics

All outputs are saved in the `results/` directory.

---

## Input Data

- VCF file containing genetic variants

Example input:

data/example_variants.vcf

---

## Analysis Steps

### 1. Variant Statistics

Script:

scripts/variant_stats.py

Calculates:

- Total number of variants
- Number of SNPs
- Number of insertions
- Number of deletions

Output:

results/variant_statistics.txt

---

## How to Run

From the root of the repository:

bash pipelines/variant_analysis/run_variant_analysis.sh

---

## Requirements

- Python >= 3.8

Install dependencies with:

pip3 install -r requirements.txt

---

## Notes

This pipeline is intended for educational and portfolio purposes.
It provides a foundation for more advanced analyses such as
cancer genomics and variant annotation.

---

## Author

Marta Sevillano
Bioinformatics MSc Student

