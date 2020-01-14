'''
StlOpenDataEtl
'''

import os
from etl import fetcher, parser, utils

CSV = '.csv'  # comma separated values
MDB = '.mdb'  # microsoft access database (jet, access, etc.)
DBF = '.dbf'  # dbase
SHP = '.shp'  # shapes

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
SUPPORTED_FILE_EXT = [CSV, MDB, DBF, SHP]

if __name__ == '__main__':
    # Fetcher
    fetcher = fetcher.Fetcher()
    src_yaml = utils.get_yaml('data/sources/sources.yml')
    responses = fetcher.fetch_all(src_yaml)

    # Parser
    parser = parser.Parser()
    for response in responses:
        try:
            response.payload = parser.flatten(response, SUPPORTED_FILE_EXT)
        except Exception as err:
            print(err)
