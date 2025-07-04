#!/usr/bin/env bash
## Plot all graphs and create all excels.
## Create one excel file at the end.

for f in scripts/plot_*
do 
echo "Processing $f"
python "$f"
done
python scripts/create_excel.py
