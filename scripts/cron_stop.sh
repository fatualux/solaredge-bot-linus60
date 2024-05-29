#!/bin/bash

# Comment out cron trigger in cron.yml
sed -i "s/^\(\s*- cron: '\)/# \1/" ../.github/workflows/cron.yml

# Commit and push changes
git add ../.github/workflows/cron.yml
git commit -m "Cron stopped."
git push origin main
