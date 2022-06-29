# Check block fail
---
## General info

This script allow you to check in the block chain if validators have failed to sign a block

## Pre-requisites

+ fullnode who can expose his API
+ the port used is 33000
+ download go and gaia
+ check if gaia is on user/go/bin
+ if no, change the path on ligne 45
+ create a ssh tunnel to ur fullnode

## Run

**step :** 

+ Go to validator.txt and write the exact name of validators that you want to work on (https://www.mintscan.io/cosmos/validators)
+ Go to config.cfg and enter the range of block that you want to check 

**different option :** 

+ --detail : give more informations about blocks (height missed block)
+ --time : give the time of execution
+ --help : display this all available option

**command :** python3 dico.py --{optionnal}

