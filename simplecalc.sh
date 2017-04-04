clear 
i="y"
echo "enter the first number"
read n1
echo "enter the second number"
read n2
while [ $i = "y" ]
do
echo "1-addition"
echo "2-subtraction"
echo "3-multiplication"
echo "4-division"
echo "5-modulo division"
read c
case $c in 
	1)sum=`expr $n1 + $n2`
	echo "result="$sum;;
	2)sum=`expr $n1 - $n2`
    echo "result="$sum;;
	3)sum=`expr $n1 \* $n2`
    echo "result="$sum;;
	4)sum=`expr $n1 / $n2`
    echo "result="$sum;;
    5)sum=`expr $n1 % $n2`
    echo "result="$sum;;
esac

echo "do you want to continue(y/n)"
read i
if [ $i != "y" ]
then 
	exit
fi
done
