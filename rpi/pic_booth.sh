#!/bin/bash

SLEEP=2

while [ 1 ] ; do 

	echo ========== 

	FILE="my_photo.jpg"
	PC="/home/eepc"
	PB="/root/picbooth"
	ILI3_ASPECT=256
	OLED_ASPECT=128
	UPLOAD_ROOT="/root/picbooth/static/img/"

	A=$(ls -1 $UPLOAD_ROOT/*jp*g 2> /dev/null)
	if [[ ! -z $A ]]; then
	   date
	   echo "Moving $A to $PC/$FILE"
	   mv $A $PC/$FILE
	else
	    echo "$UPLOAD_ROOT empty"
	fi



	if [[ -f $PC/$FILE ]]; then

	    echo "Moving $PC/$FILE to $PB"
	    mv $PC/$FILE $PB

	    cd $PB

	    OFILE="${OLED_ASPECT}.$FILE"
	    IFILE="${ILI3_ASPECT}.$FILE"
	    echo "Shrinking $FILE to $OFILE and $IFILE"
	    ./1_resize_aspect_works.py $FILE $OLED_ASPECT
	    ./1_resize_aspect_works.py $FILE $ILI3_ASPECT

	    BWFILE="bw.$OFILE"
	    echo "Processing $OFILE to $BWFILE"
	    ./2_black_white.py $OFILE

	    echo "Converting $BWFILE to frame buffer"
	    ./3_convert_to_frame_buffer.py $BWFILE 

	    echo "Processing $IFILE for ili to raw format"
	    ./4_img2rgb565.py $IFILE 
	    echo "Moving ${IFILE}.raw to /var/www/html/"
	    mv "${IFILE}".raw /var/www/html/

	else

	    echo "$PC/$FILE not present yet"

	fi 


        echo "sleep for $SLEEP secs"
	sleep $SLEEP 
	echo ========== 

done
