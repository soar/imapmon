from typing import Union
from dataclasses import dataclass


@dataclass
class Settings:

    imap_hostname: str
    imap_username: str
    imap_password: str

    channels: list

    telegram_bot_token: Union[str, None] = None
    telegram_chat_id: Union[str, None] = None
