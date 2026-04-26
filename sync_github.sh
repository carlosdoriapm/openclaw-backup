#!/bin/bash
cd "/root/.openclaw/workspaceopenclaw configure"
git add .
git commit -m "Auto-backup $(date +'%Y-%m-%d %H:%M:%S')"
git push origin main
