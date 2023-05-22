#!/usr/bin/env python

"""
Command-Line script to perform paired-end sequence trimming of FASTQ files

Similar to sickle pe
"""

import argparse 
import os
import sys

def main():
    parser = argparse.ArgumentParser (
        prog = "pet", 
        description = "Command-line script to trim paired-end reads"
    )

    # Input
    parser.add_argument("pe", help = "Paired End", \
        type=str)

    # Output
    parser.add_argument("-o", "--out",help="Write output file. " \
        "Default: stdout", metavar="FILE", type=str, required=False)
    
    # Other options
    parser.add_argument("-f", "--forward", help="Input paired-end forward fastq file.", \
        type=str, metavar="FILE", required=False)
    parser.add_argument("-r", "--reverse",help="Input paired-end reverse fastq file.", \
        type=str, metavar="FILE", required=False)
    parser.add_argument("-t", "--qual-type", help="Type of quality values: " \
            "solexa (CASAVA < 1.3), illumina (CASAVA 1.3 to 1.7), sanger (CASAVA >= 1.8)", \
            type=str, metavar="QUALITY TYPE", required=False)
    parser.add_argument("-p", "--output-pe2",help="Output trimmed reverse fastq file.", \
        type=str, metavar="FILE", required=False)
    parser.add_argument("-s", "--output-single",help="Output trimmed singles fastq file.", \
        type=str, metavar="FILE", required=False)
    
     # Parse args
    args = parser.parse_args()

    # Needs reconstruction: Load forward
    if args.forward is None:
        forward_fastq = None
    else:
        forward_fastq = args.forward
    
    # Needs reconstruction: Load reverse
    if args.reverse is None:
        reverse_fastq = None
    else:
        reverse_fastq = args.reverse

    # Needs reconstruction: Load qual_type
    if args.qual_type is None:
        quality_type = None
    else:
        quality_type = args.qual_type

    # Needs reconstruction: Set up forward output file
    if args.out is None:
        f_out_fastq = sys.stdout
    else: 
        f_out_fastq = args.out

     # Needs reconstruction: Set up reverse output file
    if args.output_pe2 is None:
        r_out_fastq = sys.stdout
    else:
        r_out_fastq = args.output_pe2

    # Needs reconstruction: Set up single output file
    if args.output_single is None:
        single_out_fastq = sys.stdout
    else:
        single_out_fastq = args.output_single

    #Testing 
    print("f:", forward_fastq)
    print("r:", reverse_fastq)
    print("t:", quality_type)
    print("o:", f_out_fastq)
    print("p:", r_out_fastq)
    print("s:", single_out_fastq)

if __name__ == "__main__":
    main()
# Print the help message: /usr/local/bin/python3 pet.py --help
# Print the tester: /usr/local/bin/python3 pet.py pe -f ~/test.f.fastq -r ~/test.r.fastq -t sanger -o ~/test.f_trimmed.fastq -p ~/test.r_trimmed.fastq -s ~/test_singletons.fastq
