"""
Utilities for mypileup
"""
import sys
from termios import TIOCPKT_DOSTOP

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def ERROR(msg):
	"""
	Print an error message and die

	Parameters
	----------
	msg : str
	   Error message to print
	"""
	sys.stderr.write(bcolors.FAIL + "[ERROR]: " + bcolors.ENDC + "{msg}\n".format(msg=msg) )
	sys.exit(1)

def GetQual(qual):
    """
    Convert qual score to ASCII
    Use encoding chr(qual+33)
    """
    #Todo

def TrimLonger(forward, reverse):
    """
    If forward FQ is longer than reverse FQ then trim
    to be the same length 

    Parameters
    ----------
    forward: fastq
    reverse: fastq
    """


"""
https://github.com/sam-k/seq-quality-trimming/blob/master/Code/seq_quality_trimming.py
"""

def write_fasta(sequences, filename, field=""):
    records = []
    for sq in sequences:
        if field=="original":
            for k in range(2):
                records.append(SeqRecord(
                        Seq(sq["seqs"][k], IUPAC.IUPACAmbiguousDNA()),
                        id=sq["names"][k], description=""))
        elif field=="trimmed" or sq["merged_seq"] is None:
            for k in range(2):
                records.append(SeqRecord(
                        Seq(sq["trimmed_seqs"][k], IUPAC.IUPACAmbiguousDNA()),
                        id=sq["names"][k], description="({})".format(
                                "unmerged" if field=="merged" else field)))
        elif field=="merged":
            records.append(SeqRecord(
                    Seq(sq["merged_seq"], IUPAC.IUPACAmbiguousDNA()),
                    id=", ".join(sq["names"]), description="(merged)"))
    SeqIO.write(records, filename, "fasta")


    


