#!/bin/bash

#
# First crappy version. No support for input parameters, yet.
# - install mencoder: sudo apt-get install mencoder
#

width=1920
height=1080

quality=70
delay=5000
#duration=15000
#duration=600000
duration=600000
#duration=60000

outputfile=mytimelapse.avi

echo `date +%H:%M:%S` "Proceed image capturing for $duration milliseconds"

raspistill -h $height -w $width -q $quality -tl $delay -t $duration -e jpg -o tl%04d.jpg

echo `date +%H:%M:%S` "Create timelapse video"
#exit 0

ls *.jpg > stills.txt

mencoder -nosound -ovc lavc \
	-lavcopts vcodec=mpeg4:aspect=16/9:vbitrate=8000000 \
	-vf scale=$width:$height \
	-mf type=jpeg:fps=24 mf://@stills.txt \
	-o $outputfile

echo `date +%H:%M:%S` "Create image backup directory "
timestamp=`date +%Y%m%d%H%M%S`
mkdir backup_$timestamp
mv tl*jpg backup_$timestamp/
rm -f stills.txt

echo `date +%H:%M:%S` "Done"

