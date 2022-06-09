#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ast import arg
import configparser
from multiprocessing.sharedctypes import Value
import requests
config = configparser.ConfigParser()
config.read('config.cfg')

def fingerprint(*args):
  d = {}
  for arg in args:
    for keys, values in config['Node'].items():
      if arg in keys:
        d[keys] = values
  return d

def node_fail_count(d):
  c = {}
  for keys in d:
    c[keys] = 0
  return c


#We can stack all the value and information in last block if we need later
last_block = requests.get(url='http://localhost:33000/blocks/latest', headers={"Content-type": "application/json"})
#print(dir(last_block)) allow us to show all the function associated to the object 'last_block'
#We used the function .json() to have only the code json and not the object 'last block'
last_block_height = last_block.json()["block"]["header"]["height"]
print(last_block_height)

def range_block(range):
  low_height = int(last_block_height) - range
  return low_height


def main():
  print(range_block(10))
  d = fingerprint("ledger", "kraken","binance","fesPFJEPF")
  print(d)
  print(node_fail_count(d))

if __name__ == "__main__":
    main()