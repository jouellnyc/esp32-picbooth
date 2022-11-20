#!/bin/bash

SLEEP=2

while [ 1 ] ; do

        FILE="my_photo.jpg"
        PC="/home/eepc"
        PB="/root/picbooth"
        ILI3_ASPECT=256
        OLED_ASPECT=128


        A=$(ls -1 /root/picbooth/static/img/*jp*g 2> /dev/null)
        if [[ ! -z $A ]]; then
           date
           echo "Moving $A to $PC/$FILE"
           mv $A $PC/$FILE
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

        else

            echo "$FILE not present yet"

        fi




        echo "sleep for $SLEEP secs"
        sleep $SLEEP

done
