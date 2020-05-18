import logging.config
import pathlib
import yaml


logging.config.dictConfig(
    yaml.load(
        pathlib.Path('imapmon/logger.yml').read_text(encoding='utf-8'),
        Loader=yaml.FullLoader
    )
)
