import logging.config
import yaml
from pathlib import Path


if not Path('.').rglob('logger.yml'):
    logging.warning('Logging configuration file not found')
else:
    for logger_config in Path('.').rglob('logger.yml'):
        logging.debug('Loading configuration file: ', logger_config)
        logging.config.dictConfig(
            yaml.load(
                logger_config.read_text(encoding='utf-8'),
                Loader=yaml.FullLoader
            )
        )
