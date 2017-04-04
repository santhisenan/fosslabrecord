#!/bin/bash
if [ $# -eq 2 ];
then
    if [ ! -f ~/classlist ] || [ $1 != "classlist" ];
    then 
        echo "file not found"
    else
        count="$(grep $2 ~/classlist | wc -l)"
        if [ $count -eq 0 ];
        then 
            echo $2 >> ~/classlist
            echo "The new claslist is "
            cat ~/classlist
        else
            echo "Name already exists in the file"
            cat ~/classlist
        fi
    fi
else
    echo "Enter the correct number of arguments : ./addnames.sh classlist
    username"
fi
