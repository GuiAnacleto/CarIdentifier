import os
import ctypes
from datetime import datetime
import sqlite3


class Config(object):

    DEBUG = False
    TESTING = False

    BABEL_DEFAULT_LOCALE = 'pt_BR'

    DEPLOY_DATE = str(datetime.now())


class ProductionConfig(Config):
    SECRET_KEY = 'KFJBkjbkÇBÇjsbnçljabnsdçjdfnpoicjbndpsjabvçasdnpçjbnpSÁJBNDF'

    DB_SERVER = '../../Database/SQNPRC001.db'

    SQLITE_DATABASE_URI = ''


class DevelopmentConfig(Config):
    SECRET_KEY = 'ÓFDJKNjolfdnÓANS´DOInafónsdofnoAKLÇPDJNFSIKJHFNASIODUFJçoldj'

    DB_SERVER = '../../Database/SQNDSC001.db'

    SQLITE_DATABASE_URI = ''
