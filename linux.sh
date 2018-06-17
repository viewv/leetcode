#!/bin/bash

i=2
while (($i<=100))
do
    j=2
    flag=1
    while [[ $j <= `expr $i/2` ]]
    do
        if [[ `expr $i % $j` == 0 ]]
        then
            flag=0;break
        fi
        j=`expr $j+1`
    done
    if [[ $flag == 1 ]]
    then
        echo "${i} is a prime!"
    fi
    i=`expr $i + 1`
done
