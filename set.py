#!/usr/bin/env python3


# TEST COMMAND
# python set.py -o output.fastq -f ~/example_files/test.f.fastq \
# -q 20 -m 30 -M 999999 pe
"""
Command-Line script to perform single-end sequence trimming of FASTQ files

Similar to sickle se
"""

import os
import sys
import argparse 
from itertools import islice

# Add the current directory to the module search path
current_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(current_dir)


def main():
    parser = argparse.ArgumentParser (
        prog = "set", 
        description = "Command-line script to trim paired-end reads"
    )

    # Input
    parser.add_argument("se", help = "Single End", \
        type=str)

    # Output
    parser.add_argument("-o", "--out",help="Write output file. " \
        "Default: stdout", metavar="FILE", type=str, required=False)
    
    # Other options
    parser.add_argument("-f", "--input", help="Input single-end fastq file.", \
        type=str, metavar="FILE", required=False)
    parser.add_argument("-t", "--qual-type", help="Type of quality values: " \
            "solexa (CASAVA < 1.3), illumina (CASAVA 1.3 to 1.7), sanger (CASAVA >= 1.8)", \
            type=str, metavar="QUALITY TYPE", required=False)
    parser.add_argument('-q', '--min-qual', default=30, nargs=1, type=int, \
            metavar="INTEGER",help='Minimum phred score. Disabled by setting it to -10.', required=False)
    parser.add_argument('-m', '--min-length', default=30, nargs=1, type=int, \
            metavar="INTEGER",help='Minimum read length after trimming.',required=False)
    parser.add_argument('-M', '--max-length', default=99999999, nargs=1, type=int,\
            metavar="INTEGER",help='Maxmimum read length after trimming.',required=False)
    
     # Parse args
    args = parser.parse_args()

    # Needs reconstruction: Load fastq
    if args.input is None:
        f_in_fastq = None
    else:
        f_in_fastq = args.input

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

    if args.min_qual is None:
        min_qual = sys.stdout
    else:
        min_qual = args.min_qual
    
    if args.min_length is None:
        min_len = sys.stdout
    else:
        min_len = args.min_length

    if args.max_length is None:
        max_len = sys.stdout
    else:
        max_len = args.max_length

    #Testing 
    print("f:", f_in_fastq)
    print("t:", quality_type)
    print("o:", f_out_fastq)
    print("q:", min_qual)
    print("m:", min_len)
    print("M:", max_len)

    def convert_qual_chars_to_scores(qual_chars):
        return [ord(char) - 33 for char in qual_chars]

    def ReadFastq(threshold, file):
        with open(file, 'r') as f:
            sequences = []
            while True:
                fastq_line = list(islice(f, 4))
                if not fastq_line:
                    break

                # Sequence and quality string
                sequence = fastq_line[1].strip()
                quality_string = fastq_line[3].strip()
                
                # Convert quality string to scores
                quality_scores = convert_qual_chars_to_scores(quality_string)

                # Filter sequence by quality score threshold
                filtered_sequence = ""
                for i in range(len(sequence)):
                    if quality_scores[i] > threshold:
                        filtered_sequence += sequence[i]
                    else:
                        break
                        
                # Add filtered sequence to list
                sequences.append(filtered_sequence)
   
        return '\n'.join(sequences)
     
    filtered_sequences = ReadFastq(min_qual, f_in_fastq)  # replace with threshold
    print(filtered_sequences)
   
if __name__ == "__main__":
    main()
# Print the help message: python3 set.py --help
# Print the tester: python3 set.py se -f ~/cse185-finalproject/example_files/test.f.fastq -t sanger -o ~/cse185-finalproject/results/test.f_trimmed.fastq
