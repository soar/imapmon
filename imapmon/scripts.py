#!/usr/bin/env python

import os
import sys
import time

import click
from dotenv import find_dotenv, load_dotenv

from imapmon.imap import IMAPClient
from imapmon.settings import Settings

sys.path.append(os.getcwd())
dotenv_file = find_dotenv(usecwd=True)
if dotenv_file:
    load_dotenv(dotenv_file, verbose=True)


@click.command(help='IMAP Monitor Tool')
@click.option(
    '--hostname', '-h',
    'imap_hostname',
    envvar='IMAP_HOSTNAME',
    required=True,
    help='IMAP server hostname'
)
@click.option(
    '--username', '-u',
    'imap_username',
    envvar='IMAP_USERNAME',
    required=True,
    help='IMAP username'
)
@click.option(
    '--password', '-p',
    'imap_password',
    envvar='IMAP_PASSWORD',
    required=True,
    help='IMAP password'
)
@click.option(
    '--channel', '-c',
    'channels',
    envvar='CHANNELS',
    required=True,
    multiple=True,
    type=click.Choice(IMAPClient.CHANNELS.keys()),
    help='Channel to retransmit messages'
)
@click.option(
    '--telegram-bot-token',
    'telegram_bot_token',
    envvar='TELEGRAM_BOT_TOKEN',
    help='Telegram Bot Token'
)
@click.option(
    '--telegram-chat-id',
    'telegram_chat_id',
    envvar='TELEGRAM_CHAT_ID',
    help='Telegram Chat ID (channel ID, group ID or @username)'
)
def run(**kwargs):
    settings = Settings(**kwargs)
    m = IMAPClient(settings)

    while True:
        m.update()
        time.sleep(10)


if __name__ == '__main__':
    run()
