#!/bin/bash
set -e

echo "Starting variant analysis pipeline..."

python3 scripts/variant_stats.py data/variants/example_variants.vcf

echo "Variant analysis pipeline completed!"

