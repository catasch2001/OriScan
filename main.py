import argparse
from scripts.skew_analysis import SkewArray, MinimumSkew
from scripts.utils import ReverseComplement

def run_oriscan():
    parser = argparse.ArgumentParser(description="OriScan: A tool for identifying replication origins in bacterial genomes.")
    parser.add_argument("genome", help="Path to the input genome file (FASTA format).")
    parser.add_argument("-o", "--output", help="Path to the output file (optional).")
    args = parser.parse_args()

    with open(args.genome, 'r') as f:
        genome_data = f.read().replace('\n', '')

    skew_array = SkewArray(genome_data)
    min_skew_positions = MinimumSkew(genome_data)

    print("Skew Array:", skew_array)
    print("Minimum Skew Positions:", min_skew_positions)

if __name__ == "__main__":
    run_oriscan()