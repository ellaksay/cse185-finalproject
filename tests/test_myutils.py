import argparse
import os
import sys
# import pytest

from ..fqutil import fastq

# TODO - add unit tests here

def test_GetQual():
	assert(fastq.GetQual(0)=="!")
