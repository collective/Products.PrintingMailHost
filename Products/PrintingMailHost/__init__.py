from Globals import DevelopmentMode

if DevelopmentMode:
    print "Hold on to your hats folks, I'm a-patchin'"
    import Patch
else:
    print "nothing to see here, move along"

def initialize(context):
    pass