#!/usr/bin/env python
from Bio import SeqIO
from sys import argv

# This script takes a fasta file as an command line argument and returns a number of
# relevant statistics like number of records, average length, largest contig

input_handle = open(argv[1], "rU")

records = SeqIO.parse(input_handle, "fasta")

num_records=0
sizetotal=0
largest_contig_size=0
largest_contig_id= ""

for record in records:
  num_records += 1
	sizetotal += len(record.seq)
	if len(record.seq) > largest_contig_size:
		largest_contig_size = len(record.seq)
		largest_contig_id = str(record.id)

print "Number of records is " + str(num_records)
print "Sum size of seqs is " + str(sizetotal)
print "Average length is " + str(sizetotal/num_records)
print "The largest contig is " + str(largest_contig_id) + " at " + str(largest_contig_size) + " bp"

input_handle.close()
