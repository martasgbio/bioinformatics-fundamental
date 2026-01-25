# Variant Analysis Pipeline

This pipeline performs a basic somatic variants analysis using VCF files.
It is designed as an educational but realistic example of a cancer genomics
workflow and as part of a profesional bioinformatics portfolio.

---

## Pipeline Overview

The pipeline includes the following steps:

1. Filtering of somatic variants from a VCF file
2. Quality and depth-based variant selection
3. Generation of a variant summary report

All outputs are saved in the `results/` directory.

---

## Input Data

- VCF file containing variants calls

Example input:

data/cancer_variants/somatic_example.vcf

---

## Analysis Steps

### 1. Somatic Variant Filtering

Script:

scripts/somatic_filter.py

Filters variants based on:

- FILTER = PASS
- DP ≥ 30

Output:

results/somatic_variants.vcf

---

### 2. Variant Summary Report

Script:

scripts/variant_report.py

Generates a summary including:

- Total number of variants
- Number of somatic variants
- SNP vs INDEL counts
- Gene-level variant counts

Output:

results/variant_report.txt

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
It reflects simplified but realistic practices used in cancer genomics
and clinical variant analysis.

---

## Author

Marta Sevillano
Bioinformatics MSc Graduate
