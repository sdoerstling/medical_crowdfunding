#!/bin/bash
for i in `seq 0 10`;
do
python 03-scrape.py $i
done
