'''cli.py

two function: decode/encode

'''
import argparse
import pathlib
from urllib.parse import urlparse

import qr

def url_type(arg):

    url = urlparse(arg)
    if all((url.scheme, url.netloc, url.path)):  # possibly other sections?
        return arg  # return url in case you need the parsed object
    raise ArgumentTypeError('Invalid URL')
    
    

class CustomFormatter(argparse.RawDescriptionHelpFormatter,
                      argparse.ArgumentDefaultsHelpFormatter):
    pass

def decode_func(args):
    pass

def encode_func(args):
    pass

def read_user_cli_args():
    '''Handle the CLI arguments and options'''
    
    parser = argparse.ArgumentParser(prog='qr',
                                     description = qr.__title__,
                                     epilog='please send complaints to /dev/null',
                                     formatter_class=CustomFormatter)

    subparsers = parser.add_subparsers(dest='subparser_name')
    ## create the parser for the 'decode' subcommand
    parser_decode = subparsers.add_parser('decode',
                                          help='Decodes the QR code')

    parser_decode.add_argument('--input',
                               type=pathlib.Path,
                               required = False,
                               help='path to the image containing the QR code')
    
    parser_decode.set_defaults(func=decode_func)

    ## https://stackoverflow.com/q/73718877
    parser_decode.add_argument('--url',
                               type=url_type,
                               required = False,
                               help='URL to the image containing the QR code')

    parser_encode = subparsers.add_parser('encode',
                                          help='Encodes data into a QR code')
    
    parser_encode.set_defaults(func=encode_func)
    
    
    
    
    
    return parser.parse_args()
