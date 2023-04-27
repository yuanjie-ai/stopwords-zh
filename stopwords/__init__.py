"""Top-level package for stopwords-zh."""
import time

__author__ = """stopwords-zh"""
__email__ = 'yuanjie@example.com'
# __version__ = '0.0.0'
__version__ = time.strftime("%Y.%m.%d.%H.%M.%S", time.localtime())

from ._stopwords import stopwords, filter_stopwords
