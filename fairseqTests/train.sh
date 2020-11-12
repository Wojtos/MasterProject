#!/bin/bash
#SBATCH -e logs/log-%j.err
#SBATCH -o logs/log-%j.out

module load plgrid/tools/python-intel/3.6.2
module load plgrid/apps/cuda/10.1

source $HOME/fairseqTests/venv/bin/activate

# cd fairseq/examples/translation
# bash prepare-wmt14en2de.sh
# cd ../../..

# TEXT=$HOME/fairseqTests/fairseq/examples/translation/wmt17_en_de
# fairseq-preprocess --source-lang en --target-lang de \
#    --trainpref $TEXT/train --validpref $TEXT/valid --testpref $TEXT/test \
#    --destdir $HOME/fairseqTests/data-bin/wmt17_en_de

mkdir -p checkpoints/fconv
fairseq-train data-bin/wmt17_en_de \
    --lr 0.25 --clip-norm 0.1 --dropout 0.2 --max-tokens 4000 \
    --arch fconv_wmt_en_de --save-dir checkpoints/fconv \
    --optimizer	adam

