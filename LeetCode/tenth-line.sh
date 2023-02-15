#!/bin/bash
filename='file.txt'

ln=1
while read p; do
    if [ $ln -eq 10 ]
    then 
    echo "$p"
    fi
    ln=$((ln+1))
done < $filename