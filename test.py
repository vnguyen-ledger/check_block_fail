#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from wsgiref.validate import validator
from typing import Sequence
import requests
from wsgiref.validate import validator
import configparser

#All node whith their finguer print
config = configparser.ConfigParser()
config['Node'] = {}
config['Node']['ledger'] = '3B845C9AF1D69E9FBB620B69AB226B28BAC97985'
config['Node']['binance'] = '83F47D7747B0F633A6BA0DF49B7DCF61F90AA1B0'
config['Node']['stakefish'] = 'AC2D56057CD84765E6FBE318979093E8E44AA18F'
config['Node']['kraken'] = '6D701FA59532688DF16BAF9521137E8C14CBB316'

with open('config.cfg', 'w') as configfile:
  config.write(configfile)

# def validator_fail(*args):

#     validator_fail_count = {}
#     for validator_fail_count in validator_hash:
#         if validator_fail_count == args:
#             validator_fail_count = 0
#     return validator_fail_count

# def var_hash(*args): #mettre les nodes en paramètre

#     validator_hash = {}
#     for var in sec:
#         if var == args:
#             validator_hash = args
#     return validator_hash

validator_hash = 1 #var_hash()

validator_fail_count = 1 #validator_fail()

# On crée un tunnel ssh vers un block signature afin qu'il se synchronise à la blockchain

#current_height = requests.get(curl -s -H "Content-Type: application/json" http://localhost:33000/blocks/latest | jq '.block.header.height' -r)


def missed_block(range, self):

    current_height = self.requests.get(method='GET', url='http://localhost:33000/blocks/latest',
                                    headers={"Content-type": "application/json"})

    low_height = current_height - range

    for block in Sequence(low_height, current_height):
        block_signature = self.requests.get(method='GET', url='http://localhost:33000/blocks/%s' %block,
                                    headers={"Content-type": "application/json"})
        for validator in validator_hash:
            if validator == False:
                validator_fail_count = validator_fail_count + 1
                print("The block" + block_signature + "has been missed at " + block)

print(validator_fail_count)

