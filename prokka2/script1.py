#!/usr/bin/env python


import sys

input_file= sys.argv[1]  

from Bio import SeqIO
for seq_record in SeqIO.parse(input_file, "fasta"):
	identity= seq_record.description
	
	if 'Typ' in identity:
                print(identity)

	if 'Typ' in identity:
               print(repr(seq_record.seq))
	
	if 'Typ' in identity:
		print(identity) >> new.txt

