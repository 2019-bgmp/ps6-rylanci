#!/usr/bin/env python3

#NAME = RYAN LANCIONE
#CONTRIBUTORS = Jared, Nick Wagner

import re
import sys
import matplotlib.pyplot as plt
import argparse 



def get_args():
	parser = argparse.ArgumentParser(description="A program to display config size distribution")
	parser.add_argument("-k", "--ksize", help="kmer size", required=True, type=int)
	parser.add_argument("-f", "--file", help="filename", required=True)
	parser.add_argument("-cc", "--cov_cutoff", help="coverage cutoff", required=True)
	return parser.parse_args()

args = get_args()
KMER_LEN=args.ksize
FILE =args.file

#FILE = "../contigs.fa"
#FILE = "../contigs_test.fa"
#FILE = "../contigs_test2.fa"
#FILE = "../contigs_test3.fa"
KMER_LEN = 49
contig_length=[]
contig_cov =[]
# script reads through fasta, selects the contig len, and coverage. Then runs stats on the groups.
with open(FILE, "r") as fh:
    for line in fh:
        if line[0] == ">":
                # a quicker way to grab only the len and the cov from the headers with reg exps would be something like...
                #  x.append(re.findall(".+_.+_(.+)_.+_(.+)", head[i], )): credit Jared
            x=[]
            x.append(re.findall("[0-9.]+", line))
#            print(x)
#            sys.exit()
#            y=[]
            #print(x)
            cl = KMER_LEN + int(x[0][1]) -1
            contig_cov.append(float(x[0][2]))
            contig_length.append(cl)
#print(contig_cov)
#print(contig_length)

'''
Adjust the k-mer length to represent the physical length. Calculate the number of
contigs, the maximum contig length, the mean contig length, and the total length of the
genome assembly across the contigs. Calculate the mean depth of coverage for the
contigs.
'''

num_contigs = len(contig_length)
mean_contig_len=(sum(contig_length)/len(contig_length))
max_contig_len= sorted(contig_length, reverse=True)
max_contig_len = max_contig_len[0]
total_len_assembly = sum(contig_length)

#KMERS_PER_REC = READ_LEN - K_SIZE + 1
#READ_LEN = KMERS_PER_REC + K_SIZE - 1
'''
adj_kmer_len=[]
for i, n in enumerate(contig_length):
    adj_kmer_len.append(contig_length[i] + KMER_LEN -  1)
#print(adj_kmer_len)
'''

#print("total: ",total_len_assembly)
contig_nuc_sum = 0                          # Calulating N50. Still needs work.
#print(sorted(contig_length))
contig_length.sort(reverse=True)
#print(contig_length)

for j in (contig_length):
    contig_nuc_sum += j
    if contig_nuc_sum > (total_len_assembly/2):
#print(j)
        break

print(j)
'''
Calculate the distribution of contig lengths and bucket the contig lengths into groups of
100bp. So, all contigs with lengths between 0 and 99 would be in the 0 bucket, those
with lengths between 100 and 199 would be in the 100 bucket, etc
'''

# creates a sum of the amount of coverage lens that fall insides groups of 100bp
bucket_dict = {}
for val in range(0,50000,100):
    bucket_dict.setdefault(val, 0)

for n in contig_length:
    if ((n // 100)*100) in bucket_dict:
        bucket_dict[(n // 100)*100] +=1

print(mean_contig_len)
print(max_contig_len)
#print(contig_length)
print(total_len_assembly)
print(num_contigs)
'''
print('#','Contig length','\t','Number of contigs in this category')
for k, v in bucket_dict.items():
    print(k,'\t',v)
'''

'''
#print(len(kmer_occ), len(kmer_freq))
#print(max(kmer_occ), max(kmer_freq))
dict_lists=sorted(bucket_dict.items())
buck_keys, buck_vals=zip(*dict_lists)

plt.plot(buck_keys, buck_vals)
plt.xlabel("Config Size in bp")
plt.ylabel("Number of Contigsin this Catagory")
plt.title("Config size dist k-{} cc-{}".format(args.ksize,args.cov_cutoff))
plt.savefig("contig_size_dist.png")
'''
