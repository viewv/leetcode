#!/bin/bash

for((i=0;i<5;i++));
do
    echo ` expr $i + 2 `
done

echo ` expr 1 + 1 `