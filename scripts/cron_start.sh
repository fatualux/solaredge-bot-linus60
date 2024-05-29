#!/bin/bash

# Add cron trigger to cron.yml
sed -i "s/^# \(\s*- cron: '\)/\1/" ../.github/workflows/cron.yml

# Commit and push changes
git add ../.github/workflows/cron.yml
git commit -m "Cron started."
git push origin main
