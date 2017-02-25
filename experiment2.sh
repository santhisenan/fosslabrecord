:'Experiment 2
SHELL PROGRAMMING
DATE : 17-02-2017
AIM

Write shell script to show various system configuration like
1.Currently logged user and his logname
2.Your current shell
3.Your home directory
4.Your operating system type
5.Your current path setting
6.Your current working directory
7.Show Currently logged number of users

'


clear
log=`who|wc -l`
echo "the currently logged in user is $USER"
echo "the current shell is $SHELL"

echo "the home drectory is  $HOME"

echo "the os type  is $OSTYPE"
echo "the current path setting is $PATH"
echo "the working directory is $PWD"
echo "there are $log users logged in"

