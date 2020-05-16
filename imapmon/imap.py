import logging
import typing

from click import BadOptionUsage
from imap_tools import MailBox, Q

from imapmon.channels.base import BaseChannel
from imapmon.channels.telegram import TelegramChannel
from imapmon.settings import Settings


logger = logging.getLogger(__name__)


class IMAPClient:

    CHANNELS = {
        'telegram': TelegramChannel
    }

    def __init__(self, settings: Settings):
        self.settings = settings
        self.mailbox = MailBox(self.settings.imap_hostname)
        self.mailbox.login(self.settings.imap_username, self.settings.imap_password)

        self.channels: typing.Dict[str, BaseChannel] = {}
        for channel_name in settings.channels:
            try:
                self.channels[channel_name] = self.CHANNELS.get(channel_name)(settings)  # noqa
            except TypeError:
                raise BadOptionUsage('channel', f'Channel {channel_name} is not defined')

    def update(self):
        for msg in self.mailbox.fetch(Q(seen=False)):
            logger.info('Found new message with ID: %s', msg.uid)
            for channel_name, channel in self.channels.items():
                channel.message(msg)
