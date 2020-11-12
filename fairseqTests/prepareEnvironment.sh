#!/bin/bash
#SBATCH -e logs/log-%j.err
#SBATCH -o logs/log-%j.out

module load plgrid/tools/python-intel/3.6.2
module load plgrid/apps/cuda/10.1

source $HOME/fairseqTests/venv/bin/activate
