#!/bin/bash
# Lab 6: Permissions in Linux
# Task: Change file owner and group and see how it affects file usage

echo "=== Step 1: Create a test file ==="
touch testfile.txt
echo "Hello, permissions!" > testfile.txt
ls -la testfile.txt

echo ""
echo "=== Step 2: View current permissions ==="
stat testfile.txt

echo ""
echo "=== Step 3: Change permissions with chmod ==="
chmod 754 testfile.txt
echo "Set permissions to 754 (rwxr-xr--)"
ls -la testfile.txt

echo ""
echo "=== Step 4: Create a test user and group ==="
sudo groupadd lab6group
sudo useradd -m -s /bin/bash lab6user
echo "Created user 'lab6user' and group 'lab6group'"

echo ""
echo "=== Step 5: Change file owner with chown ==="
sudo chown lab6user testfile.txt
echo "Changed owner to lab6user"
ls -la testfile.txt

echo ""
echo "=== Step 6: Change file group with chgrp ==="
sudo chgrp lab6group testfile.txt
echo "Changed group to lab6group"
ls -la testfile.txt

echo ""
echo "=== Step 7: Change owner and group together ==="
sudo chown lab6user:lab6group testfile.txt
echo "Changed owner:group to lab6user:lab6group"
ls -la testfile.txt

echo ""
echo "=== Step 8: Effect on file access ==="
echo "Current user ($(whoami)) is neither owner nor in lab6group."
echo "Permissions: rwxr-xr-- (754)"
echo "  - Owner (lab6user): can read, write, execute"
echo "  - Group (lab6group): can read and execute"
echo "  - Others (current user): can only read"

# Try to write as 'other' (should fail since 754 gives others only read)
echo ""
echo "Trying to write to file as current user (others permission = r--):"
if echo "test write" >> testfile.txt 2>/dev/null; then
    echo "Write succeeded (we are the file owner or root)"
else
    echo "Permission denied — write blocked as expected"
fi

echo ""
echo "=== Cleanup ==="
rm -f testfile.txt
sudo userdel -r lab6user
sudo groupdel lab6group
echo "Done."
