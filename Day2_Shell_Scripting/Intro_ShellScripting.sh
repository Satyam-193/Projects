#!/bin/bash



echo "What is system name: "
echo $(whoami)

echo "now, Enter user Name: "
read name
 
if  [ $name ]; then
	echo " It is good"
else  
	echo "Not great $name "
fi

echo $(ifconfig)



