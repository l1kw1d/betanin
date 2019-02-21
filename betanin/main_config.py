# standard library
import os
import sys
from contextlib import contextmanager

# 3rd party
import toml
from loguru import logger

# betanin
from betanin import paths


DEFAULT_CONFIG = {
    'frontend': {
        'username': '',
        'password': ''
    },
    'notifications': {
    	'services': {},
        'strings': {
            'body': '@ $time. view/use the console at http://127.0.0.1:5000/$paths.CONFIG_PATH',
            'title': '[betanin] torrent `$name` $status'
        }
    }
}


def _exists():
    return os.path.exists(paths.CONFIG_PATH)


def read():
    with open(paths.CONFIG_PATH, 'r') as file:
        return toml.load(file)


def write(config):
    with open(paths.CONFIG_PATH, 'w') as file:
        toml.dump(config, file)


@contextmanager
def mutate():
    config = read()
    yield config
    write(config)


def ensure():
    if not _exists():
        logger.error(f'config `{paths.CONFIG_PATH}`: does not exist - creating and exiting')
        write(DEFAULT_CONFIG)
        sys.exit(1)
    else:
        config = read()
        if not config['frontend'] \
                or 'password' not in config['frontend'] \
                or 'username' not in config['frontend'] \
                or not config['frontend']['username'] \
                or not config['frontend']['password']:
            logger.error(f'config `{paths.CONFIG_PATH}`: please provide a frontend username / password')
            sys.exit(1)
    logger.info(f'using config `{paths.CONFIG_PATH}`')
