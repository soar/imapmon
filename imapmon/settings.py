import logging
from dataclasses import dataclass
from pathlib import Path
from typing import Union


@dataclass
class Settings:

    imap_hostname: str
    imap_username: str
    imap_password: str

    channels: list

    telegram_bot_token: Union[str, None] = None
    telegram_chat_id: Union[str, None] = None

    log_level: Union[str, None] = None

    def __post_init__(self):
        logging.getLogger().setLevel(self.log_level)
        self.version = Path('version.txt').read_text().strip()
