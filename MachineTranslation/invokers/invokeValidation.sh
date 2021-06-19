#!/bin/bash
#SBATCH -e ../logs/log-%j.err
#SBATCH -o ../logs/log-%j.out
#SBATCH --nodes 1
#SBATCH --time=12:00:00
#SBATCH --partition=plgrid-gpu-v100
#SBATCH --gres=gpu:1
#SBATCH --account=plglemkingpu3

module load plgrid/tools/python-intel/3.6.2
module load plgrid/apps/cuda/10.1

# Run given batch
$1 do_eval
