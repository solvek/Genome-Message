from GenomeReader import GenomeReader
from tqdm import tqdm

genome_file = "ncbi/ncbi_dataset/data/GCA_000001405.29/GCA_000001405.29_GRCh38.p14_genomic.fna"
reader = GenomeReader(genome_file)

prev_line = 0
with tqdm(total=reader.size) as pbar:
    for symbol in reader:
        diff = reader.line-prev_line
        if diff > 1000:
            pbar.update(diff*80)
            prev_line = reader.line
        if reader.is_head:
            print(reader.line, reader.column)
