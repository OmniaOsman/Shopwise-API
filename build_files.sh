#!/bin/bash

# Install Python 3.10.7
curl -O https://www.python.org/ftp/python/3.10.7/Python-3.10.7.tar.xz
tar -xf Python-3.10.7.tar.xz
cd Python-3.10.7
./configure --enable-optimizations
make altinstall

# Install pip
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3.10 get-pip.py

# Install dependencies
pip3.10 install -r requirements.txt

# Collect static files
python3.10 manage.py collectstatic --noinput