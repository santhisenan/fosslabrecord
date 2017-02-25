#!/bin/bash

echo "########################OS#####################";
echo -e "`cat /etc/os-release`"
echo  "##################Available Shells###########################"
echo -e  "`cat /etc/shells`"
echo  "#################Mouse Info########################"
echo -e "`xset q`"
echo  "####################Memory Information####################"
echo -e "`cat /proc/meminfo`"
echo "#####################Hard Disk Info####################"
echo -e "Driver: `sudo hdparm -I /dev/sda`"
echo "##################File Mounted#####################"
echo -e "`cat /proc/mounts`"
