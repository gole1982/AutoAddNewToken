#!/bin/bash
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
CRON_JOB="0 0 * * * cd $SCRIPT_DIR && ./run_task.sh >> $SCRIPT_DIR/logs/cron.log 2>&1"

echo "Setting up cron job..."
echo "$CRON_JOB"

(crontab -l 2>/dev/null | grep -v "automation.py"; echo "$CRON_JOB") | crontab -

echo "Cron job installed:"
crontab -l | grep automation