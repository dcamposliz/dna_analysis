
"""
To execute this program, enter into Terminal:

	python3 script.py
"""

# importing modules
import Bio
print(Bio.__version__)
from Bio.Seq import Seq
from Bio import Alphabet

# playing around with `Seq`
mySeq = Seq("AGTACACTGGT")
print(mySeq)

Seq('AGTACACTGGT', Alphabet)

