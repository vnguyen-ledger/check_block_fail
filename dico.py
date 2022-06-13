#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from cgi import print_directory
import configparser
import json
from multiprocessing import Value
from optparse import Values
from re import A
import string
from typing import List
import requests
config = configparser.ConfigParser()
config.read('config.cfg')

#VERSION WITH INPUT

# def list_node_arg():
#   list = []
#   node = 'node'
#   while node != None:
#     node = input("enter the name of the node: ")
#     if node == 'None':
#       return list
#     else:
#       list.append(node)
#     print(list)


#VERSION WITH CONFIG FILE

def list_node_arg():
  list_node = {}
  for node, finguerprint in config['List'].items():
    list_node[node] = finguerprint
  return list_node

#VERSION WITH INPUT

# def range_arg():
#   nb = int(input("enter the range of last block: "))
#   print(nb)
#   return nb

#VERSION WITH CONFIG FILE

def range_arg():
  for keys in config['Range'].values():
    return int(keys)


def nodes_fingerprint(list_node):
  node_fingerprint = {}
  for arg in list_node:
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
  list = list_node_arg()
  fingerprint = nodes_fingerprint(list)
  fail_count= node_fail_count(fingerprint)
  print(fingerprint)
  print(fail_count)
  print(low_heigth(range_block),last_block_height())
  for block in range(low_heigth(range_block), last_block_height()):
    block_signature = requests.get(url='http://localhost:33000/blocks/%s' %block, headers={"Content-type": "application/json"})
    # print(dir(block_signature))
    # print(block_signature.json())
    for keys in fail_count:
      for keys, values in fingerprint.items():
        i = 0
      # print(json.dumps(json.loads(block_signature.text), indent=4, sort_keys=True))
        for signature in block_signature.json()["block"]["last_commit"]["signatures"]:
        # print(signature["validator_address"])
          if signature["validator_address"] == values:
            i = 1
      if i != 1:
        fail_count[keys] = fail_count[keys] +1
          # print(signature["validator_address"])
          # if signature["validator_address"] == fingerprint.values():
          #   fail_count[keys] = fail_count[keys] +1
          #   print ("node : " + keys + "  -->  height : " + block_signature.json()["block"]["header"]["height"])
  print("\nnumber of missed block for each node : ")
  print(fail_count)
  return fail_count

def main():
  arg_range = range_arg()
  print(arg_range)
  missed = missed_block(arg_range)
  with open('data.json', 'w') as mon_fichier:
	  json.dump(missed, mon_fichier, indent=4)

if __name__ == "__main__":
    main()