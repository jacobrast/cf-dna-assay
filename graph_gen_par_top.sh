#!/bin/bash

for i in {1..10..1}
do
    bash graph_gen_par.sh $i 10 &
done
