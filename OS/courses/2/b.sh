#!/bin/bash

echo Comanda: $0
echo Argumente: $1 $2 $3 $4
echo Toate argumentele: $@
shift
echo Argumente: $1 $2 $3 $4
echo Toate argumentele: $@
shift 4
echo Argumente: $1 $2 $3 $4
echo Toate argumentele: $@
echo Numarul de argumente: $#

true
echo TRUE $?

false
echo FALSE $?

