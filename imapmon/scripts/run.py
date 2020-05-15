#!/usr/bin/env python

import os
import sys

import click
from dotenv import find_dotenv, load_dotenv

sys.path.append(os.getcwd())
load_dotenv(find_dotenv(usecwd=True), verbose=True)


@click.command(help='IMAP Monitor Tool')
@click.option('--host', '-h', help='IMAP server hostname')
def run(*args, **kwargs):
    for k, v in kwargs.items():
        print(f'k: {k}, v: {v}')
