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




fileo1=/projects/bgmp/rlancio5/Bi621/ps6-rylanci/velvet_out_31
fileo2=/projects/bgmp/rlancio5/Bi621/ps6-rylanci/velvet_out_41
fileo3=/projects/bgmp/rlancio5/Bi621/ps6-rylanci/velvet_out_49


#running velvetg for each of the kmer lengths

	#velvetg kmer_len 31
/usr/bin/time -v velvetg $fileo1


	#velvetg kmer_len 41
/usr/bin/time -v velvetg $fileo2

	#velvetg kmer_len 49
/usr/bin/time -v velvetg $fileo3
