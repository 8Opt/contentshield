#!/bin/sh

# Update environment
apt-get update

apt-get install unzip

# Install virtual environment
apt install python3.10-venv
python3 -m venv cs_env
source evento_be/bin/activate

# Setup environment
echo "Start setting up the environment"
python3 -m pip install -U pip
python3 -m pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
python3 -m pip install -r requirements.txt