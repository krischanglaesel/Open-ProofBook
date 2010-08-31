# -*- coding: utf-8 -*-
from settings import *

DEBUG = TEMPLATE_DEBUG = False
DATABASE_ENGINE = 'mysql'     # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME =  'openproofbook' #PROJECT_PATH + 'cobratechtools/gpxe/sqlite.db'             # Or path to database file if using sqlite3.
DATABASE_USER = 'nang'             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''  