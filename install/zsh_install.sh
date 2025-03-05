#!/bin/sh

pip install colorama --break-system-packages
PYTHON_PATH=$(which python3)
echo "alias ppm=\"$PYTHON_PATH ~/ppm/ppm.py\"" >> ~/.zshrc
source ~/.zshrc
echo "Success!"
