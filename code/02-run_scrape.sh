#!/bin/bash
for i in `seq 0 700`;
do
python 03-scrape.py $i
done
