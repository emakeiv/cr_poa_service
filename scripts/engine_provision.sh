#!/bin/bash

# update packages and Upgrade system
sudo apt-get update && sudo apt-get upgrade -y

# install tesseract-ocr engine and all other required packages
sudo apt-get install tesseract-ocr -y

# install english language package 
sudo apt-get install tesseract-ocr-eng -y

# install lithuanian language package
sudo apt-get install tesseract-ocr-lit -y

# verify installation
tesseract --version