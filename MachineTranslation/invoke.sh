#!/bin/bash
#SBATCH -e logs/log-%j.err
#SBATCH -o logs/log-%j.out
#SBATCH --nodes 1
#SBATCH --time=1:00:00
#SBATCH --partition=plgrid-gpu-v100
#SBATCH --gres=gpu:8
#SBATCH --account=plglemkingpu3

module load plgrid/tools/python-intel/3.6.2
module load plgrid/apps/cuda/10.1

# virtualenv -p python venv
source venv/bin/activate

# Run given batch
$1
