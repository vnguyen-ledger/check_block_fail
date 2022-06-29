# Check block fail
---
## General info

This script allow you to check in the block chain if validators have failed to sign a block

## Pre-requisites

+ install click
+ install requests
+ fullnode who can expose his API
+ the port used is 33000
+ download go and gaia
+ add gaia to the PATH
+ create a ssh tunnel to your fullnode

## Run

**step :**

+ Go to validator.txt and write the exact name of validators that you want to work on (https://www.mintscan.io/cosmos/validators)
+ Go to config.cfg and enter the range of block that you want to check

**Usage:** check_block_fail.py [OPTIONS]

  displays all missed blocks for each validator in json format

**Options:**
  --detail  detail about height missed block
  --time    give the time of execution
  --help    Show this message and exit.


**command :** python3 dico.py --{optionnal}

