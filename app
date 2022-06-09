#!/bin/bash

# Declare variables
declare -A validator_hash=(
["ledger"]="3B845C9AF1D69E9FBB620B69AB226B28BAC97985"
["binance"]="83F47D7747B0F633A6BA0DF49B7DCF61F90AA1B0"
["stakefish"]="AC2D56057CD84765E6FBE318979093E8E44AA18F"
["kraken"]="6D701FA59532688DF16BAF9521137E8C14CBB316"
)

declare -A validator_fail_count=(
["ledger"]=0
["binance"]=0
["stakefish"]=0
["kraken"]=0
)

# Check is ssh tunnel is mounted
if ! nc -vz localhost 33000 > /dev/null 2>&1; then
  echo "Port not listening on 33000, exiting..."
fi

current_height=$(curl -s -H "Content-Type: application/json" http://localhost:33000/blocks/latest | jq '.block.header.height' -r)
#current_height=10384372
if [ "$#" -ne 1 ]; then
            echo "Give block range"
fi
range=$1
low_height=$( expr $current_height - $range )

for block in $(seq $low_height $current_height)
do
        block_signatures=$(curl -s -H "Content-Type: application/json" http://localhost:33000/blocks/$block)
        for validator in "${!validator_hash[@]}"
        do
                #echo " $validator - $(echo $block_signatures | jq --arg address "${validator_hash[$validator]}" '[.block.last_commit.signatures[].validator_address|contains($address)]|any')"
                if echo $block_signatures | jq --arg address "${validator_hash[$validator]}" '[.block.last_commit.signatures[].validator_address|contains($address)]|any' | grep -q false; then
                        validator_fail_count[$validator]=$( expr  ${validator_fail_count[$validator]} + 1 )
                        validator_missed_height[$validator]+=("$block")

                fi
        done
done

for validator in "${!validator_fail_count[@]}"; do echo "$validator has missed: ${validator_fail_count[$validator]}/$( expr $range + 1 ) blocks"; done



