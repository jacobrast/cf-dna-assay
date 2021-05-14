#!/bin/bash
#Make sure to activate the environment

let s=$1*1000
let n=$2*1000

for (( i=$s; i<=1000000; i = $i+$n ))
do
    python extract_loci_dis.py $i
    python gen_matrix.py ~/Desktop/data_full loci_dist_$i.txt matrix_600_dist_$i.csv 
    python nn.py matrix_600_dist_$i.csv
done
