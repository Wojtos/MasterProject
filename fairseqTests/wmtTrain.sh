#!/bin/bash
#SBATCH -e logs/log-%j.err
#SBATCH -o logs/log-%j.out

module load plgrid/tools/python-intel/3.6.2
module load plgrid/apps/cuda/10.1

source $HOME/fairseqTests/venv/bin/activate

# mkdir -p checkpoints/transformer_wmt_en_de_big
# fairseq-train data-bin/wmt17_en_de \
#  --lr 0.5 --clip-norm 0.1 --dropout 0.2 --max-tokens 4000 \
#  --criterion label_smoothed_cross_entropy --label-smoothing 0.1 \
#  --lr-scheduler fixed --force-anneal 50 \
#  --arch transformer_wmt_en_de_big --save-dir checkpoints/transformer_wmt_en_de_big \
#  --optimizer adam \
#  --keep-last-epochs 2 # --fp16

mkdir -p checkpoints/fconv_wmt_en_de
fairseq-train data-bin/wmt17_en_de \
  --lr 0.5 --clip-norm 0.1 --dropout 0.2 --max-tokens 4000 \
  --criterion label_smoothed_cross_entropy --label-smoothing 0.1 \
  --lr-scheduler fixed --force-anneal 50 \
  --arch fconv_wmt_en_de --save-dir checkpoints/fconv_wmt_en_de \
  --optimizer nag \
  --keep-last-epochs 2 # --fp16



