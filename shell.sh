#!/bin/bash
if [ -f "input.py" ];
then
python3 input.py
echo $output
elif [ -f "input.cpp" ];
then
g++ input.cpp -o input
./input
fi