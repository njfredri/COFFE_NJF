#!/bin/bash

# Check if any arguments are provided
if [ $# -eq 0 ]; then
    echo "No arguments provided."
    exit 1
fi

# Loop through each argument and print it
echo "Arguments provided:"
for arg in "$@"; do
    echo "$arg"
done
