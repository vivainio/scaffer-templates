""" Small 'replacement' for paket bootstrapper

In reality just downloads paket.bootstrapper.exe and calls it with arguments you gave to get_paket.

Must be placed in the .paket/ directory
"""

from __future__ import print_function

import urllib
import os
from os.path import abspath, dirname, isfile
import urllib
import subprocess
import sys

paket_dir = abspath(dirname(__file__))

BOOTSTRAP_NAME = "paket.bootstrapper.exe"
PAKET_NAME = "paket.exe"
BOOTSTRAP_URL = "https://github.com/fsprojects/Paket/releases/download/5.174.2/paket.bootstrapper.exe"


def get_url(url, fname):
    print("GET", url)
    urllib.urlretrieve(url, filename=fname)


def run(cmd):
    print(">", cmd)
    subprocess.check_call(cmd)


def get_paket_if_needed(argv):
    if isfile(PAKET_NAME):
        return
    if not isfile(BOOTSTRAP_NAME):
        get_url(BOOTSTRAP_URL, BOOTSTRAP_NAME)

    run([BOOTSTRAP_NAME] + argv)


def main():
    restore = False
    args = sys.argv[1:]
    if "restore" in args:
        restore = True
        args.remove("restore")

    os.chdir(paket_dir)

    get_paket_if_needed(args)
    if restore:
        run([PAKET_NAME, "restore"])


if __name__ == "__main__":
    main()
