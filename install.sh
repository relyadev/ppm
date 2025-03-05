#!/bin/bash

pip install colorama --break-system-packages
PYTHON_PATH=$(which python3)
if [[ $SHELL == *"zsh"* ]]; then
    echo "alias ppm=\"$PYTHON_PATH ~/ppm/ppm.py\"" >> ~/.zshrc
    source ~/.zshrc
elif [[ $SHELL == *"bash"* ]]; then
    echo "alias ppm=\"$PYTHON_PATH ~/ppm/ppm.py\"" >> ~/.bashrc
    source ~/.bashrc
else
    echo "Shell is not exist!"
    exit 1
fi

echo "Success!"
