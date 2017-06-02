#!/usr/bin/env python

import logging
import os

import pygsheets


class Client(object):
    def __init__(self, credential_json, doc_id, worksheet_index=0):
        self.gc = pygsheets.authorize(service_file=os.path.expanduser(
            credential_json))
        self.spreadsheet = self.gc.open_by_key(doc_id)
        self.worksheet = self.spreadsheet.worksheet('index', worksheet_index)

    def get_column(self):
        'Return the number of columns'
        return self.worksheet.cols
