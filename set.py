#!/usr/bin/env python

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
    parser.add_argument('-q', '--min-qual', default=30, type=int, \
            help='Minimum phred score. Disabled by setting it to -10.', required=False)
    
     # Parse args
    args = parser.parse_args()

    # Load fastq
    if args.input is None:
        f_in_fastq = None
    else:
        f_in_fastq = args.input

    # Load qual_type
    if args.qual_type is None:
        quality_type = None
    else:
        quality_type = args.qual_type

    # Set up output file
    if args.out is None:
        f_out_fastq = sys.stdout
    else: 
        f_out_fastq = args.out
        
    # Load phred score
    if args.min_qual is None:
        min_qual = 30
    else:
        min_qual = args.min_qual
        
    #Testing 
    print("Input fastq file(f):", f_in_fastq)
    print("Quality type(t):", quality_type)
    print("Output sequence(o):", f_out_fastq)
    print("Minimum quality score(q):", min_qual)
    
    def convert_qual_chars_to_scores(qual_chars):
        return [ord(char) - 33 for char in qual_chars]

    def filterFastq(threshold, file):
        with open(file, 'r') as input_file:
            sequences = []
            qualities = []
            while True:
                fastq_section = list(islice(input_file, 4))
                if not fastq_section or len(fastq_section) < 4:
                    break

                # Sequence and quality string
                sequence = fastq_section[1].strip()
                quality_string = fastq_section[3].strip()
                
                # Convert quality string to scores
                quality_scores = convert_qual_chars_to_scores(quality_string)

                # Filter sequence by quality score threshold
                filtered_sequence = ""
                filtered_quality = ""
                for i in range(len(sequence)):
                    if quality_scores[i] > threshold:
                        filtered_sequence += sequence[i]
                        filtered_quality += quality_string[i]
                    else:
                        break
                        
                # Add filtered sequence to list
                sequences.append(filtered_sequence)
                qualities.append(filtered_quality)
   
        return sequences, qualities
                    
    def outputFile(oFile, iFile, sequences, qualities):
        with open(oFile, 'w') as output_file, open(iFile, 'r') as input_file:
            for sequence, quality in zip(sequences, qualities):
                fastq_line = list(islice(input_file, 4))
                if not fastq_line:
                    break
                    
                # write header and '+'
                output_file.write(fastq_line[0])  # header
                output_file.write(sequence + '\n')  # sequence
                output_file.write(fastq_line[2])  # '+'
                output_file.write(quality + '\n')  # quality

    filtered_sequences, filtered_qualities = filterFastq(min_qual, f_in_fastq)
    results = outputFile(f_out_fastq, f_in_fastq, filtered_sequences, filtered_qualities) 
    
if __name__ == "__main__":
    main()
