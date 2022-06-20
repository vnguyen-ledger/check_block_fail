#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import configparser
from typing import List


config = configparser.ConfigParser()
config.read('config2.cfg')

filin = open("validator.txt", "r")
lines = filin.readlines()

def validator_txt():
  config.remove_section('List')
  config.add_section('List')
  for keys, values in config['Node'].items():
    for line in lines:
      if line.strip() == keys:
        config.set('List', keys, values)

  with open("config2.cfg", "w") as f:
    config.write(f)

def main():

  validator_txt()


if __name__ == "__main__":
    main()


