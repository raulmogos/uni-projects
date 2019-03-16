#!/bin/bash

for A in a b c; do
    echo $A din for
done

for A in a b c
do
    echo $A din for
done

for A in $@; do
    if test -f $A; then
        echo $A e fisier
    elif test -d $A; then
        echo $A e director
    elif echo $A | grep -q "^[0-9]\+$"; then
        echo $A e numar
    else
        echo nu stim ce e $A
    fi
done

for A; do
    echo $A
done

while true; do
    read X
    if test "$X" == "stop"; then
        break
    fi
done




