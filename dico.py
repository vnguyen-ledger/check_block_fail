#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import click
import configparser
import json
import requests
import timeit
import subprocess

config = configparser.ConfigParser()
config.read('config.cfg')

# def bring_moniker():
#   config = {}
#   validators = requests.get(url='http://localhost:33000/validators', headers={"Content-type": "application/json"})
#   for moniker in validators.json["description"]["moniker"]:
#     # bash = subprocess.call('./get_validator.sh')
#     # config.update({moniker : bash})
#     try:
#       config.add_section("SETTINGS")
#     except configparser.DuplicateSectionError:
#       pass

def option_arg(detail):
  '''
  return option detail/normal (--detail)
  '''
  if detail == 0:
    return 0
  return 1


def list_node_arg():
  '''
  bring validators and stack them in a list
  '''
  list_node = {}
  for node, finguerprint in config['List'].items():
    list_node[node] = finguerprint
  return list_node


def range_arg():
  '''
  bring the range of block
  '''
  for keys in config['Range'].values():
    return int(keys)


def nodes_fingerprint(list_node):
  '''
  use the validator list to build a new dict with finguerprint
  '''
  node_fingerprint = {}
  for arg in list_node:
    for node, fingerprint in config['Node'].items():
      if arg in node:
        node_fingerprint[node] = fingerprint
  return node_fingerprint


def node_fail_count(node_fingerprint):
  '''
  build a new dict to count block fail for each validator
  '''
  node_fail_count= {}
  for keys in node_fingerprint:
    node_fail_count[keys] = 0
  return node_fail_count

def last_block_height():
  '''
  return the height of the current block
  '''
  last_block = requests.get(url='http://localhost:33000/blocks/latest', headers={"Content-type": "application/json"})
  last_block_height = last_block.json()["block"]["header"]["height"]
  return int(last_block_height)

def low_heigth(range):
  '''
  return the height of the lower block in terms of range
  '''
  l = last_block_height()
  low_height =  l - range
  return low_height


def missed_block(range_block,detail):
  '''
  check for all validator if they missed a block
  then increment the value of fail block
  if --detail, give also the height of the missed block
  return a new dict
  '''
  list = list_node_arg()
  fingerprint = nodes_fingerprint(list)
  fail_count= node_fail_count(fingerprint)
  value = option_arg(detail)

  if value == 1:
    for keys in fail_count:
      list_block_height = []
      height = {'block_missed' : 0, 'height' : list_block_height }
      fail_count[keys] = height

    for block in range(low_heigth(range_block), last_block_height()):
      block_signatures = requests.get(url=f'http://localhost:33000/blocks/{block}', headers={"Content-type": "application/json"})
      signatures = block_signatures.json()["block"]["last_commit"]["signatures"]
      for key in fail_count:
        validators_address = []

        for signature in signatures:
          validators_address.append(signature["validator_address"])

        if fingerprint[key] not in validators_address:
          fail_count[key]['block_missed'] += 1
          fail_count[key]['height'].append(int(block_signatures.json()["block"]["header"]["height"])-1)

  else:
    for block in range(low_heigth(range_block), last_block_height()):
      block_signatures = requests.get(url=f'http://localhost:33000/blocks/{block}', headers={"Content-type": "application/json"})
      signatures = block_signatures.json()["block"]["last_commit"]["signatures"]
      for key in fail_count:
        validators_address = []

        for signature in signatures:
          validators_address.append(signature["validator_address"])

        if fingerprint[key] not in validators_address:
          fail_count[key] += 1

  dict = { "validator": fail_count}
  return dict

@click.command()
@click.option('--detail', is_flag=True, help='detail about height missed block')
@click.option('--time', is_flag=True, help='give the time of execution')
def main(detail,time):
  '''
  check the option to give argument to missed_block()
  build a new dict
  write the output into json file
  '''
  start = timeit.default_timer()
  if detail:
    d = option_arg(1)

  else:
    d = option_arg(0)
  arg_range = range_arg()
  range = {'range' : arg_range}
  missed = missed_block(arg_range,d)

  stop = timeit.default_timer()

  if time:
    dict_time = {'time' : stop - start}
    missed = {**dict_time,**missed}


  merge = {**range,**missed}


  with open('data.json', 'w') as file:
    json.dump(merge, file, indent=4)

if __name__ == "__main__":
    main()