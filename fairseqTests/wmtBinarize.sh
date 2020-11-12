#!/bin/bash
#SBATCH -e logs/log-%j.err
#SBATCH -o logs/log-%j.out

module load plgrid/tools/python-intel/3.6.2
module load plgrid/apps/cuda/10.1

source $HOME/fairseqTests/venv/bin/activate

TEXT=fairseq/examples/translation/wmt17_en_de
fairseq-preprocess --source-lang en --target-lang de \
  --trainpref $TEXT/train --validpref $TEXT/valid --testpref $TEXT/test \
  --destdir data-bin/wmt17_en_de --thresholdtgt 0 --thresholdsrc 0

