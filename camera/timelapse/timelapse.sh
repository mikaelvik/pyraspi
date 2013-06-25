#!/bin/bash

raspistill -h 600 -w 900 -q 70 -tl 500 -t 5000 -e jpg -o image_%04d.jpg

