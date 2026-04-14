#!/bin/bash
# Magisterial Manifold Bootstrap Script

echo "--- [MAGISTERIUM] BOOTSTRAP INITIATED ---"

# Step 1: Ensure Python is accessible
if ! command -v python3 &> /dev/null
then
    echo "[!] Python 3 could not be found. Please install Python 3.11+"
    exit 1
fi

# Step 2: Ensure environment variables are loaded
if [ ! -f .env ]; then
    echo "[*] No .env found. Copying .env.example -> .env"
    cp .env.example .env
fi

# Step 3: Install dependencies
echo "[*] Installing Python dependencies..."
python3 -m pip install --upgrade pip
python3 -m pip install -e .

# Step 4: Docker check
if ! command -v docker &> /dev/null
then
    echo "[!] Docker is NOT installed. The system will fall back to MOCK_DB=True for local execution."
    export MOCK_DB=True
    echo "export MOCK_DB=True" >> ~/.magisterium_rc
else
    echo "[*] Docker detected. You can launch full instances via 'make up'."
fi

echo "--- [MAGISTERIUM] BOOTSTRAP COMPLETE ---"
echo "You can now use 'magisterium' CLI commands natively or run 'make local-visualizer' to test graphics."
