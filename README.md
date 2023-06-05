# cse185-finalproject


## About

The use of sequencing technology such as Illumina and Solexa tend to reduce read quality across a read towards the 3' and 5' end. To compensate for this and prevent innocrrectly called bases in downstream analysis, read trimming tools are needed. 

Our tool, SET, mimicks functionality of Sickle through the use of a sliding window that uses a user set threshold to determine read quality throughout a fastq file. 

**Options**

**Single-end**
Input a single-end file (fastq, Sanger, Illumina, Solexa) and output a single-end output file of reads that passed the filter.

**Quality threshold**
User set quality threshold for filters. On a phred-scale from 0-41 for FastQ input data

## Installation
```
git clone https://github.com/ellaksay/cse185-finalproject
cd cse185-finalproject
python3 setup.py build_ext --inplace
```
## Usage Instructions
```
Example help command :
python3 set.py --help
Example command :
python3 set.py se -f <file_1.fq> -t [sanger] -o <file_1_trimmed.fq>  -q [min_qual]
Running tests : 
python3 set.py se -f ~/cse185-finalproject/example_files/test.fastq -t sanger -o ~/cse185-finalproject/results/test_trimmed.fastq -q 20
```

## Inputs and options
The following inputs are required:
- ```-f``` ```--input```: Single-end fastq read
- ```-o``` ```--output```: Output file

Users may also specify these options:
- ```-t``` ```--qual-type```: Type of quality values (sanger, illumina, solexa)
- ```-q``` ```--min-qual```: Minimum quality

## Contributors
This repository was generated for a UCSD CSE 185 Advanced Bioinformatics Lab final project by students Ella Say, Brianna Sanchez, and Anu Selvaraj




