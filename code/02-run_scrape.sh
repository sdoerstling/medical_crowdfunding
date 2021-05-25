#!/bin/bash
for i in `seq 0 10`; #change range of loop to evaluate increments of 1000 GFM campaigns
do
python 03-scrape.py $i
done
