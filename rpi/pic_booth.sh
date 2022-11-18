#!/bin/bash

SLEEP=2

while [ 1 ] ; do

        FILE="my_photo.jpg"
        PC="/home/eepc"
        PB="/root/picbooth"

        A=$(ls -1 /root/picbooth/static/img/*jpg 2> /dev/null)
        if [[ ! -z $A ]]; then
           date
           echo "Moving $A to $PC/$FILE"
           mv $A $PC/$FILE
        fi

        if [[ -f $PC/$FILE ]]; then

            echo "Moving $FILE ... "
            mv $PC/$FILE $PB

            cd $PB

            echo "Resizing $FILE ... "
            ./1_resize_aspect_works.py $FILE
            echo "Converting  $FILE ... "
            FILE="128.$FILE"

            ./3_black_white.py $FILE
            FILE="bw.$FILE"

            ./2_convert_to_frame_buffer.py $FILE

        else

            echo "$FILE not present yet"

        fi

        echo "sleep for $SLEEP secs"

        sleep $SLEEP

done

