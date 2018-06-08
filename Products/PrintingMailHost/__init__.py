from Globals import DevelopmentMode
import logging
import os

LOG = None
ENABLED = None
FIXED_ADDRESS = []

TRUISMS = ['yes', 'y', 'true', 'on']


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
       (ENABLED is None and DevelopmentMode is True):
        LOG.warning("Hold on to your hats folks, I'm a-patchin'")
        import Patch
        Patch  # pyflakes
