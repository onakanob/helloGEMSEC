#!/bin/sh

for filename in ./*.txt; do
    echo "executing say.py with $filename"
    python say.py "$filename"
done

