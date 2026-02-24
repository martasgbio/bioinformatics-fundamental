import sys
import pandas as pd
import matplotlib.pyplot as plt

input_file = sys.argv[1]
output_prefix = sys.argv[2]

# Leer archivo como tabla
df = pd.read_csv(input_file, sep="\t")

# Eliminar posibles filas no numéricas
df = df[pd.to_numeric(df["count"], errors="coerce").notnull()]
df["count"] = df["count"].astype(int)

# Ordenar y seleccionar top 20
df = df.sort_values(by="count", ascending=False)
top20 = df.head(20)

# Guardar tabla
top20.to_csv(f"{output_prefix}_top20.tsv", sep="\t", index=False)

# Calcular frecuencia relativa
total = df["count"].sum()
top20["frequency"] = top20["count"] / total

plt.figure()
plt.bar(top20["kmer"], top20["frequency"])
plt.yscale("log")
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig(f"{output_prefix}_top20_relative_log.png")

