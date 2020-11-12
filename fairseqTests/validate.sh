#!/bin/bash
#SBATCH -e logs/log-%j.err
#SBATCH -o logs/log-%j.out

module load plgrid/tools/python-intel/3.6.2
module load plgrid/apps/cuda/10.1

source $HOME/fairseqTests/venv/bin/activate

fairseq-generate data-bin/wmt17_en_de \
    --path $HOME/fairseqTests/checkpoints/fconv/checkpoint1.pt \
    --batch-size 128 --beam 5 # | tee $SCRATCH/gen.out

# fairseq-generate data-bin/wmt14.en-de.newstest2014  \
#    --path data-bin/wmt14.en-de.fconv-py/model.pt \
#    --beam 5 --batch-size 128 --remove-bpe | tee $SCRATCH/gen.out
# ...
# | Translated 3003 sentences (96311 tokens) in 166.0s (580.04 tokens/s)
# | Generate test with beam=5: BLEU4 = 40.83, 67.5/46.9/34.4/25.5 (BP=1.000, ratio=1.006, syslen=83262, reflen=82787)

# Compute BLEU score
# grep ^H $SCRATCH/gen.out | cut -f3- > $SCRATCH/gen.out.sys
# grep ^T $SCRATCH/gen.out | cut -f2- > $SCRATCH/gen.out.ref
# fairseq-score --sys $SCRATCH/gen.out.sys --ref $SCRATCH/gen.out.ref
# BLEU4 = 40.83, 67.5/46.9/34.4/25.5 (BP=1.000, ratio=1.006, syslen=83262, reflen=82787)
