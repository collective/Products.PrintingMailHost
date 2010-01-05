import logging
import email.Parser
try:
    from email.message import Message
except ImportError:
    from email import Message
from base64 import decodestring

from AccessControl import ClassSecurityInfo
from Products.MailHost.MailHost import MailBase

LOG = logging.getLogger('PrintingMailHost')
PATCH_PREFIX = '_monkey_'

__refresh_module__ = 0


def monkeyPatch(originalClass, patchingClass):
    """Monkey patch original class with attributes from new class
       (Swiped from SpeedPack -- thanks, Christian Heimes!)

    * Takes all attributes and methods except __doc__ and __module__
      from patching class
    * Safes original attributes as _monkey_name
    * Overwrites/adds these attributes in original class
    """
    for name, newAttr in patchingClass.__dict__.items():
        # don't overwrite doc or module informations
        if name not in ('__doc__', '__module__'):
            # safe the old attribute as __monkey_name if exists
            # __dict__ doesn't show inherited attributes :/
            orig = getattr(originalClass, name, None)
            if orig:
                stored_orig_name = PATCH_PREFIX + name
                stored_orig = getattr(originalClass, stored_orig_name, None)
                # don't double-patch on refresh!
                if stored_orig is None:
                    setattr(originalClass, stored_orig_name, orig)
            # overwrite or add the new attribute
            setattr(originalClass, name, newAttr)


class PrintingMailHost:
    """MailHost which prints to output."""
    security = ClassSecurityInfo()

    security.declarePrivate('_send')
    def _send(self, mfrom, mto, messageText, debug=False, immediate=False):
        """Send the message."""
        if isinstance(messageText, str):
            messageText = email.Parser.Parser().parsestr(messageText)
        base64_note = ""
        print
        print " ---- sending mail ---- "
        print "From:", mfrom
        print "To:", mto
        if messageText.get('Content-Transfer-Encoding') == 'base64':
            base64_note = "NOTE: The email payload was originally base64 " \
                          "encoded.  It was decoded for debug purposes."
            body = messageText.get_payload()
            if isinstance(body, list):
                for attachment in body:
                    if isinstance(attachment, Message):
                        messageText.set_payload(
                            decodestring(attachment.get_payload()))
                        break
                    elif isinstance(attachment, str):
                        messageText.set_payload(decodestring(attachment))
                        break
            else:
                messageText.set_payload(decodestring(body))

        print messageText
        print " ---- done ---- "
        print
        if base64_note:
            print base64_note
            print


LOG.warn("""

******************************************************************************

Monkey patching MailHosts to print emails to the terminal instead of
sending them.

NO MAIL WILL BE SENT FROM ZOPE AT ALL!

Turn off debug mode or remove PrintingMailHost from the Products
directory to turn this off.

******************************************************************************
""")

monkeyPatch(MailBase, PrintingMailHost)

# Patch some other mail host implementations.
try:
    from Products.SecureMailHost.SecureMailHost import SecureMailBase
except ImportError:
    pass
else:
    monkeyPatch(SecureMailBase, PrintingMailHost)

try:
    from Products.MaildropHost.MaildropHost import MaildropHost
except ImportError:
    pass
else:
    monkeyPatch(MaildropHost, PrintingMailHost)

try:
    from Products.SecureMaildropHost.SecureMaildropHost import \
        SecureMaildropHost
except ImportError:
    pass
else:
    monkeyPatch(SecureMaildropHost, PrintingMailHost)
