'''cli.py'''

import argparse
import pathlib

import qr

class CustomFormatter(argparse.RawDescriptionHelpFormatter,
                      argparse.ArgumentDefaultsHelpFormatter):
    pass

def read_user_cli_args():
    '''Handle the CLI arguments and options'''
    
    parser = argparse.ArgumentParser(
        prog='qr',
        description = qr.__title__,
        formatter_class=CustomFormatter)
    
    return parser.parse_args()
