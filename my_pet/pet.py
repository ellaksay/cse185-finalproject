#!/usr/bin/env python

"""
Command-Line script to perform paired-end sequence trimming of FASTQ files

Similar to sickle pe
"""

import argparse 
import os
import sys
from . import myutils as myutils

def main():
    parser = argparse.ArgumentParser (
        prog = "pet", 
        description = "Command-line script to trim paired-end reads"
    )

    # Input
    parser.add_argument("se", help = "Single End", \
        type=str)
    
    # Output
    parser.add_argument("-o", "--out",help="Write output file." \
        "Default: stdout", metavar="FILE", type=str, required=False)
    
    # Other options
    parser.add_argument("-f", "--forward", help="Input paired-end forward fastq file.", \
        type=str, metavar="FILE", required=False)
    parser.add_argument("-r", "--reverse",help="Input paired-end reverse fastq file.", \
        type=str, metavar="FILE", required=False)
    parser.add_argument("-p", "--output-pe2",help="Output trimmed reverse fastq file.", \
        type=str, metavar="FILE", required=False)
    parser.add_argument("-s", "--output-single",help="Output trimmed singles fastq file.", \
        type=str, metavar="FILE", required=False)


     # Parse args
    args = parser.parse_args()

    # Set up output file
    if args.out is None:
        outf = sys.stdout
    else: outf = open(args.out, "w")

    # Needs reconstruction: Load FASTA
    if args.forward is not None:
        if not os.path.exists(args.forward):
            myutils.ERROR("{fastq} does not exist".format(fastq=args.forward))
        forward_fastq = args.forward
    else:
        forward_fastq = None

if __name__ == "__main__":
    main()
# Print the help message: /usr/local/bin/python3 pet.py --help
