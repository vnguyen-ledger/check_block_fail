
#!/bin/bash


#Build SSH tunnel
ssh -L 33000:localhost:33000 cosmos-stg-01


res = `./gaiad debug pubkey `./gaiad query staking validators --node tcp://10.99.0.248:23000 --chain-id cosmoshub-4 -o json --limit 300| jq '.validators[]| select(.description.moniker == "hongkong-chain")' |jq -r '"\(.consensus_pubkey)"'``
echo res

