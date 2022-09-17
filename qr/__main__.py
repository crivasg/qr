
'''__main__.py '''

from qr.cli import read_user_cli_args

import pathlib
import sys

if __name__ == '__main__':
    if len(sys.argv)==1:
        sys.exit(-1)

    args = read_user_cli_args()
    args.func(args)
