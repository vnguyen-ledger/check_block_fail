#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ast import arg
import configparser
from multiprocessing.sharedctypes import Value
from optparse import Values
from this import d
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
    
    print(keys, d[keys])
  return c


def main():
  d = fingerprint("ledger", "kraken","binance","fesPFJEPF")
  print(node_fail_count(d))

if __name__ == "__main__":
    main()