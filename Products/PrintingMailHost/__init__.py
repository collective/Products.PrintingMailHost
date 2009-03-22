from Globals import DevelopmentMode
import os

TRUISMS = ['yes', 'y', 'true', 'on']
ENABLED = os.environ.get('ENABLE_PRINTING_MAILHOST', None)

# check to see if the environment var is set to a 'true' value
if (ENABLED is not None and ENABLED.lower() in TRUISMS) or \
   (ENABLED is None and DevelopmentMode is True):
    print "Hold on to your hats folks, I'm a-patchin'"
    import Patch

def initialize(context):
    pass
