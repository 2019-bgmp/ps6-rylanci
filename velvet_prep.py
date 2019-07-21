#!/usr/bin/env python3





F =["/projects/bgmp/shared/Bi621/800_3_PE5_interleaved.fq_1","/projects/bgmp/shared/Bi621/800_3_PE5_interleaved.fq_2","/projects/bgmp/shared/Bi621/800_3_PE5_interleaved.fq.unmatched"] 
#F = "ps6pt2_test.fq"

#total nucleotide prediction 
fosmids= 50
fos_lens = 40000
p_total_nuc = fosmids * fos_lens


#calculating actual total nucleotides
 
seq_list=[]
for i in F:
	with open(i, "r") as fh:
		for i,l in enumerate(fh):
			if i%4 == 1:
				seq_list.append(len(l.strip()))
				
#print(seq_list)i
num_reads = len(seq_list)
total_nuc=sum(seq_list)
exp_cov=(total_nuc/p_total_nuc)
avg_seq_len = total_nuc/num_reads
#print(exp_cov)
#print(avg_seq_len)




# kmer_coverage = (expected kmer coverage * kmers per record) / average sequence length
# reminder: kmers_per_record= read_len - k_size - 1
kpr31 =  avg_seq_len -31 -1
kpr41 = avg_seq_len -41 -1
kpr49 = avg_seq_len -49 -1
Kmer_cov31=(exp_cov * kpr31) / avg_seq_len
Kmer_cov41=(exp_cov * kpr41) / avg_seq_len
Kmer_cov49=(exp_cov * kpr49) / avg_seq_len

print(Kmer_cov31)
print(Kmer_cov41)
print(Kmer_cov49)
# Add optional step of calculating "correct coverage and correct  kmer coverage if time. 
