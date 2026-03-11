import argparse
from Bio import SeqIO
from scripts import SkewArray, MinimumSkew, GenerateSkewPlot

def run_oriscan():
    parser = argparse.ArgumentParser(description="OriScan: A tool for identifying replication origins in bacterial genomes.")
    parser.add_argument("genome", help="Path to the input genome file (FASTA format).")
    args = parser.parse_args()

    record = SeqIO.read(args.genome, "fasta")
    genome_data = str(record.seq).upper()

    print(f"Analyzing genome: {record.id}")
    skew_array = SkewArray(genome_data)
    min_skew_positions = MinimumSkew(genome_data)

    print("Skew Array:", skew_array)
    print("Minimum Skew Positions:", min_skew_positions)

    GenerateSkewPlot(skew_array, record.id)
    
if __name__ == "__main__":
    run_oriscan()