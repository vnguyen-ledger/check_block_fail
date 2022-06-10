#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ast import arg
import configparser
from logging.config import valid_ident
from multiprocessing import Value
from platform import node
import string
from wsgiref.validate import validator
import requests
config = configparser.ConfigParser()
config.read('config.cfg')


def list_node_arg():
  list = []
  node = 'node'
  while node != None:
    node = input("enter the name of the node: ")
    if node == 'None':
      return list
    else:
      list.append(node)
    print(list)

def range_arg():
  nb = int(input("enter the range of last block: "))
  print(nb)
  return nb

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
  fail= node_fail_count(fingerprint)
  print(fingerprint)
  print(fail)
  print(low_heigth(range_block),last_block_height())
  for block in range(low_heigth(range_block), last_block_height()):
    block_signature = requests.get(url='http://localhost:33000/blocks/%s' %block, headers={"Content-type": "application/json"})
    # print(dir(block_signature))
    # print(block_signature.json())
    for keys in fail:
      # if block_signature.json()[".block.last_commit.signatures[].validator_address"] == False:
      fail [keys] = fail[keys] +1
  print("missed block for each node : ")
  print(fail)

  return block

def main():
  arg_range = range_arg()
  missed_block(arg_range)

if __name__ == "__main__":
    main()