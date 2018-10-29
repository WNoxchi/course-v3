#!/bin/bash
# Wayne Nixalo | 20181028
# ============================================== #
# see Google Images Download:
# https://github.com/hardikvasa/google-images-download
# see fast.ai forum thread:
# https://forums.fast.ai/t/tips-for-building-large-image-datasets/26688
# ============================================== #

export path=$HOME/data/aircraft

for c in f16 su24 mig29 su22 su25 mig21 fa18ef f4 a10 \
    cargo f15e fighters f15c typhoon fa18c f35 su30 su27 \
    tornado j20 mig25 rafale f14 f22 su57 mig31 su34 jas39

do
    googleimagesdownload -k $c -s medium -l 500 -o $path -i train/$c -cd $HOME/chromedriver
done
