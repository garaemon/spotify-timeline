#!/usr/bin/env python

import os
import logging

import coloredlogs
from emoji import emojize

from .spreadsheet import Client


class Application(object):
    SPREADSHEET_CREDENTIAL_JSON = '~/.raspi-home-secrets/google_spreadsheet.json'

    def __init__(self):
        coloredlogs.install()

    def check(self):
        if 'GOOGLE_SPREADSHEET_FOR_SPOTIFY' not in os.environ:
            logging.error('environmental variable'
                          'GOOGLE_SPREADSHEET_FOR_SPOTIFY is required')
            return False
        else:
            logging.info(emojize(':heavy_check_mark:'
                                 'GOOGLE_SPREADSHEET_FOR_SPOTIFY '
                                 'defined'))
        if not os.path.exists(os.path.expanduser(
                self.SPREADSHEET_CREDENTIAL_JSON)):
            logging.error('{} does not exists'.format(
                self.SPREADSHEET_CREDENTIAL_JSON))
            return False
        else:
            logging.info(emojize(':heavy_check_mark: {} exists.'.format(
                self.SPREADSHEET_CREDENTIAL_JSON)))

        logging.info(emojize(':heavy_check_mark: Everything looks good!'))
        return True

    def read_test(self):
        client = Client(self.SPREADSHEET_CREDENTIAL_JSON,
                        os.environ['GOOGLE_SPREADSHEET_FOR_SPOTIFY'])
        client.get_column()
        logging.info(emojize(':heavy_check_mark: Success to read spread sheet!'))
        return True
