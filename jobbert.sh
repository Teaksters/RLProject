#!/bin/bash

#SBATCH --job-name=test
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --time=24:00:00
#SBATCH --mem=32000M
#SBATCH --output=test.out

module purge
module load 2019
module load Python/3.7.5-foss-2019b
# module load CUDA/10.1.243
# module load cuDNN/7.6.5.32-CUDA-10.1.243
# module load NCCL/2.5.6-CUDA-10.1.243
module load Anaconda3/2018.12

# Your job starts in the directory where you call sbatch
cd $HOME/
# Activate your environment

conda activate rlcourse
# Run your code
srun python -u RLProject/test.py
