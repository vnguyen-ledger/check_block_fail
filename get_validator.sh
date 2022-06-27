#!/bin/bash

cd
cd go/bin/

echo #1

./gaiad debug pubkey $1 2>&1 | head -n-1 | awk '{print $2}'
