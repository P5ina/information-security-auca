#!/bin/bash
# Lab 9: Package Management in Linux
# Task: Install and explore the nginx package

echo "=== Step 1: Update package list ==="
sudo apt update

echo ""
echo "=== Step 2: Search for nginx ==="
apt search nginx 2>/dev/null | head -10

echo ""
echo "=== Step 3: Check nginx dependencies ==="
apt-cache depends nginx

echo ""
echo "=== Step 4: Install nginx ==="
sudo apt install -y nginx

echo ""
echo "=== Step 5: Verify installation ==="
nginx -v
which nginx
dpkg -l nginx

echo ""
echo "=== Step 6: Check nginx status ==="
sudo systemctl status nginx --no-pager

echo ""
echo "=== Step 7: Start nginx and test ==="
sudo systemctl start nginx
echo "Fetching localhost..."
curl -s http://localhost | head -5

echo ""
echo "=== Step 8: Explore nginx files ==="
echo "-- Config file --"
cat /etc/nginx/nginx.conf | head -20

echo ""
echo "-- Default site config --"
cat /etc/nginx/sites-enabled/default | head -20

echo ""
echo "=== Step 9: Remove nginx ==="
sudo systemctl stop nginx
sudo apt remove -y nginx
sudo apt purge -y nginx
sudo apt autoremove -y
echo "nginx removed."

echo ""
echo "=== Done ==="
