#!/bin/bash

# Create a conda env (site) for this project
# conda create -n site python=3.10.12
~/miniconda3/envs/site/python.exe src/main.py

# Start the web server after generating the site
~/miniconda3/envs/site/python.exe server.py