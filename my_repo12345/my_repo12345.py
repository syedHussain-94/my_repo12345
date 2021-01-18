#!/usr/bin/env python3
# coding: utf-8
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""
This app is created from Dolly McDolly
"""
import os
import sys
import logging
import argparse

from core.my_repo12345 import DollyDolly, DollyDollyException
from core.config import DollyDollyConf


class DollyDollyCommandLine(object):
    """
    Command-line interface for DollyDolly
    """
    HOME = os.path.dirname(os.path.abspath(__file__))
    VERSION = "0.1.0"
    CONFIG_PATH = os.path.relpath(os.path.join(HOME, 'conf'))
    DOLLYDOLLY_CONFIG = os.path.join(CONFIG_PATH, 'my_repo12345.json')

    @classmethod
    def parse_args(cls):
        parser = argparse.ArgumentParser(
            description='DollyDolly Runtime',
            prog=__file__,
            add_help=False,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            epilog='The exit status is 0 for non-failures and 1 for failures.')

        m = parser.add_argument_group('Mandatory Arguments')
        g = m.add_mutually_exclusive_group(required=True)
        g.add_argument(
            '-foob',
            metavar='foo',
            type=str,
            help='foo')

        o = parser.add_argument_group('Optional Arguments')
        o.add_argument(
            '-my_repo12345',
            metavar='file', type=argparse.FileType(),
            default=cls.DOLLYDOLLY_CONFIG,
            help='DollyDolly configuration')
        o.add_argument(
            '-verbosity',
            metavar='{1..5}',
            default=2,
            type=int,
            choices=list(range(1, 6, 1)),
            help='Level of verbosity for logging module.')
        o.add_argument(
            '-h', '-help', '--help',
            action='help',
            help=argparse.SUPPRESS)
        o.add_argument(
            '-version',
            action='version',
            version='%(prog)s {}'.format(cls.VERSION),
            help=argparse.SUPPRESS)

        return parser.parse_args()

    @staticmethod
    def pair_to_dict(args):
        return dict(kv.split('=', 1) for kv in args)

    @classmethod
    def main(cls):
        args = cls.parse_args()

        logging.basicConfig(
            format='[DollyDolly] %(asctime)s %(levelname)s: %(message)s',
            level=args.verbosity * 10,
            datefmt='%Y-%m-%d %H:%M:%S')

        logging.info('Loading DollyDolly configuration from %s' % args.my_repo12345.name)
        try:
            my_repo12345_conf = DollyDollyConf(args.my_repo12345.read())
        except DollyDollyException as msg:
            logging.error(msg)
            return 1

        my_repo12345 = DollyDolly(my_repo12345_conf)
        try:
            pass
        except DollyDollyException as msg:
            logging.error(msg)
            return 1
        except KeyboardInterrupt:
            print('')
            logging.info("Caught SIGINT - Aborting.")
            return 0
        finally:
            logging.info("Initiating shutdown routines.")
            try:
                pass
            except DollyDollyException as msg:
                logging.error(msg)
                return 1

        return 0


if __name__ == '__main__':
    sys.exit(DollyDollyCommandLine().main())
