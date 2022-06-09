#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from ast import arg
import configparser
from platform import node
import string
import requests
config = configparser.ConfigParser()
config.read('config.cfg')

# def range_arg():
#   nb = int(input("enter the range of last block"))
#   print(nb)
#   return nb

# def list_node_arg():
#   list = []
#   node = input(string("enter the name of the node"))
#   if node == "end":
#     return list
#   else:
#     list.append(node)
#     list_node_arg()
#   print(list)

def nodes_fingerprint(*args):
  node_fingerprint = {}
  for arg in args:
    for node, fingerprint in config['Node'].items():
      if arg in node:
        node_fingerprint[node] = fingerprint
  return node_fingerprint

def node_fail_count(node_fingerprint):
  node_fail_count= {}
  for keys in node_fingerprint:
    node_fail_count[keys] = 0
  return node_fail_count


def last_block_height():
  last_block = requests.get(url='http://localhost:33000/blocks/latest', headers={"Content-type": "application/json"})
  last_block_height = last_block.json()["block"]["header"]["height"]
  return int(last_block_height)

def low_heigth(range):
  l = last_block_height()
  low_height =  l - range
  return low_height

def missed_block(range_block):
  print(low_heigth(range_block),last_block_height())
  for block in range(low_heigth(range_block), last_block_height()):
    block_signature = requests.get(url='http://localhost:33000/blocks/%s' %block, headers={"Content-type": "application/json"})
    print(dir(block_signature))
    print(block_signature.json())
    # for validator in :
    #   if block_signature.json()

  return block

def main():
  print(low_heigth(10))
  d = nodes_fingerprint("ledger", "kraken","binance","fesPFJEPF")
  print(d)
  print(node_fail_count(d))
  missed_block(10)

if __name__ == "__main__":
    main()