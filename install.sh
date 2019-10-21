#!/bin/bash

# Install dependencies
sudo apt-get install libnotify-bin

# Move the script
sudo cp -R . /usr/local/bin/gbtw-script

# Expose the script.sh file as gbtw
cd /usr/local/bin/gbtw-script && sudo pipenv install psutil && sudo mv script.sh ../gbtw
