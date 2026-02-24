# Metagenomics Analysis Pipeline

## Overview

This pipeline implements a structured metagenomic workflow starting from raw Illumina paired-end FASTQ files to downstream diversity analysis and quality-controlled comparative outputs.

The objective is to demonstrate practical handling of shotgun sequencing data, quality control interpretation, trimming effects assessment, and k-mer-based diversity estimation.

---

## Input Data

- Paired-end FASTQ files (public SRA dataset)
- Illumina sequencing platform
- Read length ~150 bp

---

## Workflow

Raw FASTQ  
↓  
FastQC quality assessment  
↓  
MultiQC summary report  
↓  
Adapter and quality trimming (fastp)  
↓  
Post-trimming statistics  
↓  
k-mer frequency counting  
↓  
Shannon diversity estimation  
↓  
Raw vs Trimmed comparison  

---

## 1️⃣ Quality Control (FastQC / MultiQC)

Initial quality assessment identified:

- Standard Illumina quality decay toward 3’ ends
- Presence of adapter-related sequence content
- Normal GC distribution for environmental microbial sample

MultiQC was used to aggregate QC metrics across samples.

---

## 2️⃣ Trimming (fastp)

Trimming was performed to:

- Remove low-quality bases
- Eliminate residual adapter contamination
- Improve downstream reliability

### Observed effects:

- Reduction in total read count
- Slight increase in GC content
- Removal of ambiguous / low-complexity reads

This is consistent with quality filtering removing low-confidence sequence regions.

---

## 3️⃣ k-mer Analysis

A Python-based k-mer counting script was implemented to:

- Parse FASTQ files
- Count k-mer frequencies
- Estimate diversity using Shannon entropy

### Metrics computed:

- Total number of k-mers
- Relative abundance of top k-mers
- Shannon diversity index

---

## 4️⃣ Raw vs Trimmed Comparison

Comparison of raw and trimmed datasets showed:

| Metric | Raw | Trimmed |
|--------|------|----------|
| Total k-mers | Higher | Lower |
| Shannon diversity | Slightly higher | Slightly reduced |

Interpretation:

- Trimming reduces total k-mer count due to read filtering
- Shannon diversity remains stable, indicating that trimming did not distort overall compositional complexity
- Diversity stability suggests biological signal preservation

---

## Key Concepts Demonstrated

- FASTQ parsing with Biopython
- k-mer frequency modeling
- Shannon diversity estimation
- Data normalization for relative abundance plots
- Pipeline modularization
- Reproducible analysis structure

---

## Limitations

- No taxonomic profiling (e.g., MetaPhlAn) due to local storage constraints
- Functional pathway inference not implemented in this version
- Diversity analysis based on k-mers rather than species-level assignments

---

## Future Extensions

- Taxonomic profiling (MetaPhlAn or Kraken2)
- Functional pathway inference (HUMAnN)
- Alpha and beta diversity metrics
- Health-marker oriented microbial scoring framework
- Automation via workflow manager (Snakemake)

---

## Technical Stack

- Python 3.10
- Biopython
- FastQC
- MultiQC
- fastp
- Linux CLI
- Git version control


