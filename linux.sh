#!/bin/bash

i=1
until ((i > 100))
do
    echo $i
    i=`expr $i + 1`
done

