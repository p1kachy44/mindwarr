#!/bin/sh
# Launcher script for Telegram Motivation Bot

# Check if Python is available
if command -v python3 >/dev/null 2>&1; then
    PYTHON_CMD="python3"
elif command -v python >/dev/null 2>&1; then
    PYTHON_CMD="python"
else
    echo "Error: Python is not installed"
    exit 1
fi

# Launch the application
echo "Starting Web Demo Application"
$PYTHON_CMD simple_web_demo.py