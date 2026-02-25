# 🧬 Bioinformatics Fundamentals & Applied Genomic Pipelines

This repository contains a modular bioinformatic workflows developed to strengthen and demonstrate practical skills in computational genomic, variant analysis, and metagenomic.

The goal of this project is to build a structured, reproducible, and transparent bioinformatics portfolio with real data, interpretable results, and scalable pipeline design.


## 📁 Repository Structure

```plaintext
bioinformatics-fundamentals/
├── data/ # Example input datasets (FASTA, VCF, FASTQ)
├── results/ # Structured output directories
├── scripts/ # Modular Python analysis scripts
├── pipelines/ # Executable workflow wrappers (bash)
│ ├── basic_analysis/
│ └── variant_analysis/
├── requirements.txt # Python dependencies
└── README.md
```
## 🛠  Pipelines Included

### 1. Basic Sequence Analysis

**Location:** `pipelines/basic_analysis/`

Exploratory analysis of DNA sequences in FASTA format:
- Sequence length statistics 
- GC content estimation
- Sliding window GC analysis
- ORF (Open Reading Frame) detection
- Codon usage analysis

### Skills demonstrated

- FASTA parsing with Biopython
- Sequence feature extraction
- Visualization of genomic metrics
- Modular scripting design

---

### 🧪 2. Variant Analysis

**Location:** `pipelines/variant_analysis/`

Introductory worklflow for processing  VCF files:

- Variant parsing
- SNP and indel statistics
- Basic filtering logic 
- Generation of summary reports

This module establishes a foundation for more advance workflows such as somaticvariant filtering and cancer genomics pipelines. 

### Skills demonstrated

- VCF handling
- Variant classification 
- Structured result reporting 
- Workflow modularization 


---

## 🦠 3. Metagenomics Analysis

**Location:** `pipelines/metagenomics_analysis/`

Shotgun metagenomic workflow starting from raw paired-end FASTQ files:

- Quality control (FastQC, MultiQC)
- Adapter and quality trimming (fastp)
- Read-level statistics
- k-mer frequency analysis
- Shannon diversity estimation
- Raw vs trimmed dataset comparison

### Key concepts demonstrated

- FASTQ parsing
- k-mer modeling
- Alpha diversity estimation
- QC interpretation
- Reproducible pipeline structuring
- Comparative dataset analysis

This pipeline reflects practical microbiome data handling and prepares the ground for future taxonomic and functional profiling extensions.


---


## 🛠  Technologies Used

- Python 3
- Bash (Linux CLI)
- Biopython
- Matplotlib
- FastQC
- MultiQC
- fastp
- Git & GitHub


---


## 🎯 Motivation
This repository represents a structured transition from foundational bioinformatics scripting to applied, workflow-oriented computational genomics.

The focus is on:

- Clean and readable code
- Reproducibility
- Logical pipeline organization
- Clear biological interpretation
- Transparent documentation


---


## 🚀 Future Extensions

- Taxonomic profiling (MetaPhlAn / Kraken2)
- Functional pathway inference (HUMAnN)
- Automated workflow management (Snakemake / Nextflow)
- Microbiome-derived health marker modeling
- Cancer-oriented somatic variant refinement



## 👤 Author
Marta Sevillano
Bioinformatics MSc Graduate

