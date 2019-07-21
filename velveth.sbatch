#!/usr/bin/env bash

#SBATCH --account=bgmp          ### SLURM account which will be charged for the job
#SBATCH --partition=bgmp        ### Partition (like a queue in PBS)
#SBATCH --job-name=PS6          ### Job Name
#SBATCH --output=slurm-%j-%x.out         ### File in which to store job output
#SBATCH --error=velvet.err          ### File in which to store job error messages
#SBATCH --time=0-01:00:00       ### Wall clock time limit in Days-HH:MM:SS
#SBATCH --nodes=1               ### Node count required for the job (usually 1)
#SBATCH --ntasks-per-node=1     ### Nuber of tasks to be launched per Node (usually 1)
#SBATCH --cpus-per-task=8       ### Number of cpus (cores) per task
#SBATCH --mail-user=rlancio5@uoregon.edu
#SBATCH --mail-type=ALL




# Part 1: velveth for kmer_lens 31, 41, 49

file1=/projects/bgmp/shared/Bi621/800_3_PE5_interleaved.fq_1
file2=/projects/bgmp/shared/Bi621/800_3_PE5_interleaved.fq_2
file3=/projects/bgmp/shared/Bi621/800_3_PE5_interleaved.fq.unmatched
fileo1=/projects/bgmp/rlancio5/Bi621/ps6-rylanci/velvet_out_31
fileo2=/projects/bgmp/rlancio5/Bi621/ps6-rylanci/velvet_out_41
fileo3=/projects/bgmp/rlancio5/Bi621/ps6-rylanci/velvet_out_49

# velveth command schematic: Program outputfile kmerlength filetype readtype files (if desired repeat:filetype readtype files)
# velvetgcommand schematic: velvetg output_directory/ -ins_length 400 -exp_cov 21.3 
	

	# velveth kmer_len 31
/usr/bin/time -v velveth $fileo1 31 -fastq -shortPaired -separate $file1 $file2 -fastq -short $file3

	# velveth kmer len 41
/usr/bin/time -v velveth $fileo2 41 -fastq -shortPaired -separate $file1 $file2 -fastq -short $file3

	# velveth kmer len 49
/usr/bin/time -v velveth $fileo3 49 -fastq -shortPaired -separate $file1 $file2 -fastq -short $file3


	#velvetg kmer_len 31
#/usr/bin/time -v velvetg $fileo1 -ins_length 76.79104993766992 -exp_cov 98.5912995

