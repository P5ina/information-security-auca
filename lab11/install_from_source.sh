#!/bin/bash
# Lab 11: Installing packages from source
# Demonstrates two methods: make install (neofetch) and ./configure + make (htop)

# ── Method 1: git clone + make install (neofetch) ──────────────────────────
echo "=== Method 1: Install neofetch from source (git + make) ==="

echo "-- Installing dependencies --"
sudo apt update -q
sudo apt install -y git make

echo "-- Cloning repository --"
git clone --depth=1 https://github.com/dylanaraps/neofetch.git /tmp/neofetch-src

echo "-- Installing --"
cd /tmp/neofetch-src
sudo make install

echo "-- Verifying --"
neofetch --version
neofetch

echo ""
echo "-- Removing neofetch --"
sudo make uninstall
cd ~
rm -rf /tmp/neofetch-src
echo "neofetch removed."

# ── Method 2: ./configure + make (htop) ────────────────────────────────────
echo ""
echo "=== Method 2: Install htop from source (./configure + make) ==="

echo "-- Installing build dependencies --"
sudo apt install -y build-essential libncursesw5-dev autoconf automake

echo "-- Cloning repository --"
git clone --depth=1 https://github.com/htop-dev/htop.git /tmp/htop-src

echo "-- Configuring --"
cd /tmp/htop-src
./autogen.sh
./configure

echo "-- Compiling --"
make -j$(nproc)

echo "-- Installing --"
sudo make install

echo "-- Verifying --"
htop --version

echo ""
echo "-- Removing htop --"
sudo make uninstall
cd ~
rm -rf /tmp/htop-src
echo "htop removed."

echo ""
echo "=== Done ==="
