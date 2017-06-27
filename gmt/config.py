#!/usr/bin/env python

import os
basedir = os.path.abspath(os.path.dirname(__file__))
# database path
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'gmt.sqlite')
# change this
SECRET_KEY = 'm1edflksndf213r0sufjmfg1saaqe'
SQLALCHEMY_TRACK_MODIFICATIONS = False
PORT = 5000
DEBUG = False
