#!/bin/bash

# Exit on error
set -e

echo "=== Binance Futures Trading Bot Setup ==="

# Check for Python
if ! command -v python3 &> /dev/null
then
    echo "Error: python3 could not be found. Please install Python 3.x"
    exit 1
fi

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

# Activate and install
echo "Installing dependencies..."
./venv/bin/pip install --upgrade pip
./venv/bin/pip install -r requirements.txt

# Create .env from template if it doesn't exist
if [ ! -f .env ]; then
    echo "Creating .env from template..."
    cp .env.example .env
    echo "Warning: Please update .env with your real API keys!"
fi

echo "=== Setup Complete! ==="
echo "To run the bot: source venv/bin/activate && python cli.py --help"
