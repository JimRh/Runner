#!/bin/bash
if [ -f "input.py" ];
then
python input.py
elif [ -f "input.cpp" ];
then
g++ input.cpp -o input
./input
fi