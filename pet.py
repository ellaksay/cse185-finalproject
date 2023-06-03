#!/usr/bin/env python


# TEST COMMAND
# python pet.py -o output.fastq -f ~/example_files/test.f.fastq \
# -q 20 -m 30 -M 999999 pe
"""
Command-Line script to perform paired-end sequence trimming of FASTQ files

Similar to sickle pe
"""

import os
import sys
import argparse 

# Add the current directory to the module search path
current_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(current_dir)

from fqutil import myutils


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
    parser.add_argument('-q', '--min-qual', default=30, nargs=1, type=int, \
            help='Minimum phred score. Disabled by setting it to -10.', required=False)
    parser.add_argument('-m', '--min-length', default=30, nargs=1, type=int, \
            help='Minimum read length after trimming.',required=False)
    parser.add_argument('-M', '--max-length', default=99999999, nargs=1, type=int,\
            help='Maxmimum read length after trimming.',required=False)
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
    print("f:", forward_fastq)
    print("r:", reverse_fastq)
    print("t:", quality_type)
    print("o:", f_out_fastq)
    print("p:", r_out_fastq)
    print("s:", single_out_fastq)
    print("q:", min_qual)
    print("m:", min_len)
    print("M:", max_len)


    fastq_in = forward_fastq
    fastq_out = f_out_fastq

    
    # read file and print back lines that pass the filter
    while True:
        read = fastq_in.get_read()
        if read is None:
            break  # EOF
        qual = [read[3], parser.encoding]
        
        # get indices of acceptable quality
        start = -1
        for q in qual:
            start += 1
            if q >= min_qual:
                break
        end = 0
        for q in reversed(qual):
            end -= 1
            if q >= min_qual:
                break
        if min_len <= len(qual) - start + end <= max_len:
            fastq_out.writelines([
                read[0], read[1][start:end] + '\n', 
                read[2], read[3][start:end] + '\n'])
    fastq_in.close()
    fastq_out.close()

if __name__ == "__main__":
    main()
# Print the help message: /usr/local/bin/python3 pet.py --help
# Print the tester: /usr/local/bin/python3 pet.py pe -f ~/test.f.fastq -r ~/test.r.fastq -t sanger -o ~/test.f_trimmed.fastq -p ~/test.r_trimmed.fastq -s ~/test_singletons.fastq
