#!/usr/bin/env python

import logging
import os
import sys
import time

import click
import requests
from dotenv import find_dotenv, load_dotenv

from imapmon.imap import IMAPClient
from imapmon.settings import Settings


logger = logging.getLogger(__name__)
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
    help='IMAP password/key/token'
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
    '--spam-filter',
    'spam_filters',
    multiple=True,
    type=str,
    help='Strings to filter messages'
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
@click.option(
    '--log-level', '-l',
    'log_level',
    envvar='LOG_LEVEL',
    type=click.Choice(logging._nameToLevel.keys()),  # noqa
    help='Log level for console messages'
)
@click.option(
    '--sentry-dsn',
    'sentry_dsn',
    envvar='SENTRY_DSN',
    help='Sentry DSN (see: sentry.io)'
)
@click.option(
    '--scan-interval',
    type=int,
    default=30,
    help='Time between checks (seconds)'
)
@click.option(
    '--push-test-url',
    help='URL to ping while running, can be used for passive monitoring'
)
def run(scan_interval: int, push_test_url: str, **kwargs):
    settings = Settings(**kwargs)
    m = IMAPClient(settings)

    logger.info('App started, version: %s', settings.version)

    while True:
        m.update()

        if push_test_url:
            resp = requests.get(push_test_url)
            logger.debug('Push test URL response: [%s] %s', resp.status_code, resp.text[:64])

        logger.debug('Sleeping for %d seconds...', scan_interval)
        time.sleep(scan_interval)
