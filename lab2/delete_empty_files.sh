#!/bin/bash

dir="$1"

if [ ! -d "$dir" ]; then
  echo "Error: '$dir' is not a valid directory"
  exit 1
fi

while IFS= read -r -d '' file; do
  echo "Deleting: $file"
  rm "$file"
  found=1
done < <(find "$dir" -maxdepth 1 -type f -empty -print0)

