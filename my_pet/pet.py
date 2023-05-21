#!/usr/bin/env python

"""
Command-Line script to perform paired-end sequence trimming of FASTQ files

Similar to sickle pe
"""

import argparse 

def main():
    parser = argparse.ArgumentParser (
        prog = "pet", 
        description = "Command-line script to trim paired-end reads"
    )

    # Input
    parser.add_argument("se",help = "Single End",\
        type=str)
    
    # Output
    parser.add_argument("-o" "--out",help="Write output file." \
        "Default: stdout",metavar="FILE",type=str,required = False)
    
    # Other options
    parser.add_argument("-f" "--forward",help="Forward read." \
        "Default: stdout",metavar="FILE",type=str,required = False)
    parser.add_argument("-r" "--reverse",help="Reverse read." \
        "Default: stdout",metavar="FILE",type=str,required = False)
    
     # Parse args
    args = parser.parse_args()
    
if __name__ == "__main__":
    main()
# Running: /usr/local/bin/python3 pet.py --help
