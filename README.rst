Products.PrintingMailHost
=========================

This is a hack. :)

This product, when installed, will check if Zope is running in debug mode,
and if so, monkey patch (that is, grab the internals of, squeeze tight, then
rip hard, just like monkeys do) Zope's MailHost class, meaning that *any and
all* uses of a MailHost will be "fixed" so that instead of sending mail, it
prints messages to the zope event log.

This is useful if you don't have a local mailhost for testing, or if you
prefer not to spam the crap out of yourself whilst finding out if your bulk
mail script is working.

If Zope is not running in debug mode, it will not install itself. However,
I wouldn't recommend putting it on a production site. You never know what
those monkeys may get up to...

You can optionally enable the PrintingMailHost with an environment variable
as of version 0.3.  See the installation instructions for more information
about how to use it.


Compatibility
-------------

Works on Plone 3.3, Plone 4, Plone 5.0, 5.1 and 5.2 (in Python 2.7, 3.6 and 3.7).


Author
------

Martin Aspeli <optilude (AT) gmx (DOT) net>
    Initial idea, release management


Contributors
------------

Dorneles Tremea <deo (AT) plonesolutions (DOT) com>
    Fixed to work both with old-style and new-style classes. Extended
    to also patch SecureMailBase from SecureMailHost, if available.

Clayton Parker <clayton (AT) sixfeetup (DOT) com>

Maurits van Rees <maurits (AT) vanrees (DOT) org>

Harald Friessnegger <harald (AT) webmeisterei (DOT) com>


Products.PrintingMailHost Installation
======================================

To install Products.PrintingMailHost into your Plone instance in
buildout, you can do this:

- Add ``Products.PrintingMailHost`` to the list of eggs to install, e.g.::

    [instance]
    ...
    eggs =
        ...
        Products.PrintingMailHost

- If you want to enable PrintingMailHost when debug-mode is off::

    [instance]
    ...
    environment-vars =
        ...
        ENABLE_PRINTING_MAILHOST True

- If you want to disable PrintingMailHost when debug-mode is on::

    [instance]
    ...
    environment-vars =
        ...
        ENABLE_PRINTING_MAILHOST False

- If PrintingMailHost is enabled, and you *additionally* want to send
  each email to a fixed address, you can add another environment
  variable::

    [instance]
    ...
    environment-vars =
        ...
        PRINTING_MAILHOST_FIXED_ADDRESS admin@example.org

  Or multiple addresses separated by spaces::

        PRINTING_MAILHOST_FIXED_ADDRESS one@example.org two@example.org

  For clarity: this first prints the email, with the original
  recipient address, and then sends an actual email with the same
  contents to the fixed address you have specified.  The original
  recipient is visible in the ``To:`` field.  It is similar to
  receiving a blind carbon copy (bcc) of an email, except that the
  original recipient never gets the email.

- Re-run buildout in order to make any of the above changes active::

    $ ./bin/buildout
