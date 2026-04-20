#!/bin/bash
# Script: check_nested_git.sh
# Purpose: Perform safe sanity checks and list/flag nested .git directories

echo "Starting sanity checks for nested .git directories..."

# 1. Check if current directory is inside a git repo
if git rev-parse --is-inside-work-tree > /dev/null 2>&1; then
  echo "Current directory is inside a git repository."
else
  echo "Warning: Current directory is NOT inside a git repository."
fi

# 2. List all nested .git directories excluding the top-level .git
echo "Searching for nested .git directories (excluding top-level)..."
nested_git_dirs=$(find . -type d -name ".git" -not -path "./.git")

if [ -z "$nested_git_dirs" ]; then
  echo "No nested .git directories found."
else
  echo "Nested .git directories found:"
  echo "$nested_git_dirs"
fi

# 3. Flag suspicious zero-byte files
echo "Checking for suspicious zero-byte files named 'git' or 'change.diff'..."
find . -type f \( -name "git" -o -name "change.diff" \) -size 0 -print

echo "Sanity checks completed."
