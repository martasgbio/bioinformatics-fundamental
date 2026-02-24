import sys

vcf_file = sys.argv[1]
output_file = sys.argv[2]

with open(vcf_file) as vcf, open(output_file, "w") as out:
    for line in vcf:
        if line.startswith("#"):
            out.write(line)
            continue

        fields = line.strip().split("\t")
        if len(fields) < 8:
            continue

        filt = fields[6]
        info = fields[7]

        # Filter: only PASS variants
        if filt != "PASS":
            continue

        # Filter by depth
        dp = None
        for entry in info.split(";"):
            if entry.startswith("DP="):
                dp = int(entry.split("=")[1])

        if dp is None or dp < 30:
            continue

        out.write(line)

