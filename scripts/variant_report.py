import sys
from collections import Counter

vcf_file = sys.argv[1]
output_file = sys.argv[2]

total_variants = 0
snps = 0
indels = 0
genes = Counter()

with open(vcf_file) as vcf:
    for line in vcf:
        if line.startswith("#"):
            continue

        fields = line.strip().split("\t")
        if len(fields) < 8:
            continue

        total_variants += 1

        ref = fields[3]
        alt = fields[4]
        info = fields[7]

        # SNP vs INDEL
        if len(ref) == 1 and len(alt) == 1:
            snps += 1
        else:
            indels += 1

        # Gene annotation
        for entry in info.split(";"):
            if entry.startswith("GENE="):
                gene = entry.split("=")[1]
                genes[gene] += 1

with open(output_file, "w") as out:
    out.write("Variant Summary Report\n")
    out.write("======================\n\n")
    out.write(f"Total somatic variants: {total_variants}\n")
    out.write(f"SNPs: {snps}\n")
    out.write(f"INDELs: {indels}\n\n")

    out.write("Variants per gene:\n")
    for gene, count in genes.items():
        out.write(f"- {gene}: {count}\n")
