"""
Cambridge is a terminal version of Cambridge Dictionary.
The dictionary data comes from https://dictionary.cambridge.org
If you're not satisfied with the result, you can try with "-w" flag to look up the word in Merriam-Webster Dictionary.
"""

import sqlite3
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cambridge.args import parse_args
from cambridge.cache import DB
# from .utils import timer


# Test fzf preview under development env
# python main.py l | fzf --preview 'python main.py  -w {}'

# @timer
def main():
    try:
        con = sqlite3.connect(
            DB, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES
        )
        cur = con.cursor()

        args = parse_args()
        args.func(args, con, cur)

        cur.close()
        con.close()

    except KeyboardInterrupt:
        print("\nStopped by user")


main()
