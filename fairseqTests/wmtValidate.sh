#!/bin/bash
#SBATCH -e logs/log-%j.err
#SBATCH -o logs/log-%j.out

module load plgrid/tools/python-intel/3.6.2
module load plgrid/apps/cuda/10.1

source $HOME/fairseqTests/venv/bin/activate

# fairseq-generate data-bin/wmt17_en_de \
#  --path checkpoints/checkpoint_previous.pt \
#  --beam 5 --remove-bpe --max-tokens 4000 | tee $SCRATCH/gen.out

 fairseq-generate data-bin/wmt17_en_de \
  --path checkpoints/fconv_wmt_en_de/checkpoint_best.pt \
  --beam 5 --remove-bpe | tee $SCRATCH/gen.out


grep ^H $SCRATCH/gen.out | cut -f3- > $SCRATCH/gen.out.sys
grep ^T $SCRATCH/gen.out | cut -f2- > $SCRATCH/gen.out.ref
fairseq-score --sys $SCRATCH/gen.out.sys --ref $SCRATCH/gen.out.ref

