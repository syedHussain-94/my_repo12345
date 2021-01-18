# coding: utf-8
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
import logging


class DollyDollyException(Exception):
    """
    Unrecoverable error in DollyDolly.
    """
    pass


class DollyDolly(object):
    """
    DollyDolly base class.
    """

    def __init__(self, conf):
    	self.conf = conf