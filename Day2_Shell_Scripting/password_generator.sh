#!/bin/bash

echo "This is a simple password generator"
echo "Enter the lenght of the password: "
read PASS_LEN

for p in $(seq 1 5);
do
	openssl rand -base64 48 | cut -c1-$PASS_LEN
done
