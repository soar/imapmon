import logging
import typing

from click import BadOptionUsage
from imap_tools import MailBox, Q

from imapmon.channels.base import BaseChannel
from imapmon.channels.tg import TelegramChannel
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
            channel_class = self.CHANNELS.get(channel_name)
            if channel_class:
                self.channels[channel_name] = channel_class(settings)
            else:
                raise BadOptionUsage('channel', f'Channel {channel_name} is not defined')

    def update(self):
        for msg in self.mailbox.fetch(Q(seen=False)):
            logger.info('Found new message with ID: `%s`, from: `%s`', msg.uid, msg.from_)
            logger.debug(' ... subject: `%s`, date: `%s`', msg.subject, msg.date_str)
            for _, channel in self.channels.items():
                channel.message(msg)
