#!/bin/bash

find ~ -type f | while read F; do
    S=`ls -l $F | awk '{print $5}'`
    if test $S -gt 10000000; then
        ls -l $F
    fi
done

