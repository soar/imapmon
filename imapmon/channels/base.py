from abc import ABCMeta, abstractmethod

from imap_tools import MailMessage

from imapmon.settings import Settings


class BaseChannel(metaclass=ABCMeta):

    settings: Settings

    def __init__(self, settings: Settings) -> None:
        self.settings: Settings = settings
        self.check_settings()

    @abstractmethod
    def check_settings(self) -> None:
        pass

    @abstractmethod
    def message(self, msg: MailMessage) -> None:
        pass
