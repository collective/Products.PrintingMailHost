from Globals import DevelopmentMode
import logging
import os

LOG = logging.getLogger('PrintingMailHost')


TRUISMS = ['yes', 'y', 'true', 'on']
ENABLED = os.environ.get('ENABLE_PRINTING_MAILHOST', None)
FIXED_ADDRESS = os.environ.get('PRINTING_MAILHOST_FIXED_ADDRESS', '')
# Treat as a list:
FIXED_ADDRESS = [addr for addr in FIXED_ADDRESS.strip().split(' ') if addr]
# check to see if the environment var is set to a 'true' value
if (ENABLED is not None and ENABLED.lower() in TRUISMS) or \
   (ENABLED is None and DevelopmentMode is True):
    LOG.warning("Hold on to your hats folks, I'm a-patchin'")
    import Patch
    Patch  # pyflakes


def initialize(context):
    pass
