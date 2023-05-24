# cse185-finalproject


## About

The use of sequencing technology such as Illumina and Solexa tend to reduce read quality across a read towards the 3' and 5' end. To compensate for this and prevent innocrrectly called bases in downstream analysis, read trimming tools are needed. 

Our tool, PET, mimicks functionality of Sickle through the use of a sliding window that uses a user set threshold to determine read quality throughout a fastq file. 

**Options**

**Single-end**
Input a single-end file (fastq, Sanger, Illumina, Solexa) and output a single-end output file of reads that passed the filter.

**Paired-End**
Input either:
- One interleaved paired-end file OR
- Two seperate input files, foward and reverse
and output either:
- one interleaved paired-end file with reads that passed the filter OR
- two output files, foward and reverse, with corresponding reads that passed the filter

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
python3 ~/cse185-finalproject/my_pet/pet.py --help
Example command :
python3 ~/cse185-finalproject/my_pet/pet.py pe -f file_1.fq -r file_2.fq -t sanger -o file_1_trimmed.fq  -p file_2_trimmed.fq -s file_single_trimmed.fq

Run tests : 
python3 ~/cse185-finalproject/my_pet/pet.py pe -f ~/test.f.fastq -r ~/test.r.fastq -t sanger -o ~/test.f_trimmed.fastq -p ~/test.r_trimmed.fastq -s ~/test_singletons.fastq
```

## Inputs and options
The following inputs are required:
- ```-f``` ```--forward```: Forward fastq read
- ```-r``` ```--reverse```: Reverse fastq read
- ```-t``` ```--qual-type```: Type of quality values 
- ```-o``` ```--output```: Forward output file
- ```-p``` ```--output-pe2```: Reverse output file
- ```-s``` ```--output-single```: Singlton output file

