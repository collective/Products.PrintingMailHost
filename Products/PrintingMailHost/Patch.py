import email.Parser
try:
    from email.message import Message
except ImportError:
    from email import Message
from base64 import decodestring

from AccessControl import ClassSecurityInfo
from Products.PrintingMailHost import LOG, FIXED_ADDRESS
from Products.MailHost.MailHost import MailBase
from StringIO import StringIO

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
        orig_messageText = messageText
        if isinstance(messageText, str):
            messageText = email.Parser.Parser().parsestr(messageText)
        base64_note = ""
        out = StringIO()
        print >> out, ""
        print >> out, " ---- sending mail ---- "
        print >> out, "From:", mfrom
        print >> out, "To:", mto
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

        print >> out, messageText
        print >> out, " ---- done ---- "
        print >> out, ""
        if base64_note:
            print >> out, base64_note
            print >> out, ""
        LOG.info(out.getvalue())
        if FIXED_ADDRESS:
            # Send a real email to the given fixed address.
            orig_send = getattr(self, PATCH_PREFIX + '_send', None)
            if orig_send is not None:
                LOG.info('Sending actual email to %s', FIXED_ADDRESS)
                # We do not pass the 'debug' and 'immediate' keyword
                # arguments, because not all implementations accept
                # both keyword arguments.
                orig_send(mfrom, FIXED_ADDRESS, orig_messageText)


warning = ("""

******************************************************************************

Monkey patching MailHosts to print e-mails to the terminal.
""")


if FIXED_ADDRESS:
    warning += ("""
Also, ALL MAIL WILL BE SENT TO ONE ADDRESS: %s

Change PRINTING_MAILHOST_FIXED_ADDRESS in the environment variables
to change the address, or remove it to only print the e-mails.
""" % FIXED_ADDRESS)
else:
    warning += ("""
This is instead of sending them.

NO MAIL WILL BE SENT FROM ZOPE AT ALL!
""")

warning += ("""
Turn off debug mode or remove Products.PrintingMailHost from the eggs
or remove ENABLE_PRINTING_MAILHOST from the environment variables to
return to normal e-mail sending.

See https://pypi.python.org/pypi/Products.PrintingMailHost

******************************************************************************
""")
LOG.warn(warning)

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
