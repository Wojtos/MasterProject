#!/bin/bash
#SBATCH -e logs/log-%j.err
#SBATCH -o logs/log-%j.out

module load plgrid/tools/python-intel/3.6.2
module load plgrid/apps/cuda/10.1

source $HOME/fairseqTests/venv/bin/activate

fairseq-interactive \
    --path checkpoints/fconv_wmt_en_de/checkpoint_best.pt data-bin/wmt17_en_de \
    --beam 5 --source-lang en --target-lang de \
    --tokenizer moses \
    --bpe subword_nmt --bpe-codes fairseq/examples/translation/wmt17_en_de/code

