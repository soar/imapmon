# pylint:disable=unsubscriptable-object

import logging
from dataclasses import dataclass
from pathlib import Path
from typing import Union

import sentry_sdk


@dataclass
class Settings:

    imap_hostname: str
    imap_username: str
    imap_password: str

    channels: list

    spam_filters: list

    telegram_bot_token: Union[str, None] = None
    telegram_chat_id: Union[str, None] = None

    sentry_dsn: Union[str, None] = None

    log_level: Union[str, None] = None

    def __post_init__(self):
        if self.log_level:
            logging.getLogger().setLevel(self.log_level)

        self.version = Path('version.txt').read_text().strip()

        if self.sentry_dsn:
            sentry_sdk.init(self.sentry_dsn)
