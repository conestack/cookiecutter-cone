#!/bin/sh
rm -r ./lib ./include ./local ./bin ./share
python3 -m venv .
./bin/pip install --upgrade pip
./bin/pip install setuptools 'zc.buildout==3.0.0b4'
./bin/buildout -c buildout.cfg -v
