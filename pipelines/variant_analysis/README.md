# Variant Analysis Pipeline

This pipeline performs a basic analysis of genetic variants from a VCF file.
It is designed as an introductory workflow for variant processing and as a
foundation for more advanced analyses such as cancer genomics.

---

## Pipeline Overview

The pipeline includes the following steps:

1. Parsing a VCF file
2. Basic variant statistics
3. Summary of variant types

All outputs are saved in the `results/` directory.

---

## Input Data

- Variant Call Format (VCF) file
- Example input file:

      data/exmple.vcf

---

## Analysis Steps

### 1. Variant Parsing and Statistics

Script:
        scripts/variant_stats.py


For each variant, the script extracts:
- Chromosome
- Position
- Reference allele
- Alternate allele

It computes:
- Total number of variants
- Number of SNPs and indels

Output:
       results/variant_statistics.txt


---

## How to Run

From the root of the repository:

```bash
bash pipelines/variant_analysis/run_variant_analysis.sh


Requeriments: 
- Python >= 3.8

No external libraries are required for this pipeline. 

Notes: 

This pipeline is intentionally simple and educational. 
It can be extended to include: 
- Variant filtering
- Functional annotation
- Cancer-related mutation analysis 

Author: 
Marta Sevillano

Bioinformatics MSc Student 


