#!/bin/bash

set -e

wget -nv https://bootstrap.pypa.io/get-pip.py
python get-pip.py
rm get-pip.py