#!/bin/bash

WORK_END_HOUR=18
WORK_END_MINUTE=00

current_hour=$(date +%H)
current_minute=$(date +%M)
current_time=$(date +%H:%M)

current_total=$((current_hour * 60 + current_minute))
end_total=$((WORK_END_HOUR * 60 + WORK_END_MINUTE))
remaining=$((end_total - current_total))

echo "Current time: $current_time"

if [ $remaining -le 0 ]; then
  echo "Work day has ended! 🎉"
else
  hours=$((remaining / 60))
  minutes=$((remaining % 60))

  echo "Work day ends after $hours hours and $minutes minutes"
fi

