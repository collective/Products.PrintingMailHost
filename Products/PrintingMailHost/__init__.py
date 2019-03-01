# -*- coding: utf-8 -*-
from App.config import getConfiguration

import logging
import os

LOG = None
ENABLED = None
FIXED_ADDRESS = []

TRUISMS = ['yes', 'y', 'true', 'on']
DevelopmentMode = False


def initialize(context):
    global LOG
    global FIXED_ADDRESS
    global ENABLED
    LOG = logging.getLogger('PrintingMailHost')

    ENABLED = os.environ.get('ENABLE_PRINTING_MAILHOST', None)
    addresses = os.environ.get('PRINTING_MAILHOST_FIXED_ADDRESS', '')
    FIXED_ADDRESS = [addr for addr in addresses.strip().split(' ') if addr]

    # check to see if the environment var is set to a 'true' value
    if (ENABLED is not None and ENABLED.lower() in TRUISMS) or \
       (ENABLED is None and getConfiguration().debug_mode is True):
        # DevelopmentMode is checked by plone.api
        DevelopmentMode = True  # noqa
        LOG.warning("Hold on to your hats folks, I'm a-patchin'")
        from Products.PrintingMailHost import Patch
        Patch  # pyflakes
