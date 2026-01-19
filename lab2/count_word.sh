#!/bin/bash

grep -o -w "$1" "$2" | wc -l | tr -d ' '  # macOS fix
