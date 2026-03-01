#!/bin/bash
# Lab 5: User Management in Linux
# Task: Discover user groups, create new user and add him to new created group

echo "=== Existing groups ==="
cat /etc/group

echo ""
echo "=== Creating new group 'lab5group' ==="
sudo groupadd lab5group
echo "Group created."

echo ""
echo "=== Creating new user 'lab5user' ==="
sudo useradd -m -s /bin/bash lab5user
echo "User created."

echo ""
echo "=== Adding lab5user to lab5group ==="
sudo usermod -aG lab5group lab5user
echo "User added to group."

echo ""
echo "=== Verifying: groups of lab5user ==="
groups lab5user

echo ""
echo "=== Verifying: lab5group in /etc/group ==="
grep lab5group /etc/group

echo ""
echo "=== Cleanup ==="
sudo userdel -r lab5user
sudo groupdel lab5group
echo "User and group deleted."
