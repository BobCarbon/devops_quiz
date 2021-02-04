#!/bin/bash
# Script to remove all files named 'virus' in /usr dir

find /usr/ -name "virus*" -exec rm {} \;