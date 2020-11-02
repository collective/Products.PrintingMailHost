Changelog
=========

1.1.5 (2020-11-02)
------------------

- Fix support for MailHost 4.10 (see `issue 33 <https://github.com/zopefoundation/Products.MailHost/issues/33>`_).
  [pbauer]


1.1.4 (2020-06-10)
------------------

- Fixed ``SyntaxError`` in previous release.  [tareqalam]


1.1.3 (2020-06-10)
------------------

- Encoding fix for Python 3
  [ajung]


1.1.2 (2019-03-05)
------------------

- Restore compatability with plone.api.
  [pbauer]


1.1.1 (2019-02-28)
------------------

- Add support Python 3
  [pbauer]


1.1.0 (2018-06-08)
------------------

- Check environment variables in Zope2 `initialize` instead of import time.
  This allows to configure environment-vars in zope.conf and use them when
  starting the instance with slc.zopescript
  [fRiSi]

1.0 (2016-09-20)
----------------

- Treat ``FIXED_ADDRESS`` as a list.  Previously, depending on your
  Plone version. a fixed address could get interpreted as a list of
  single-character email addresses, which of course does not work.
  Now it works properly.  You can also give a list of addresses by
  separating them using spaces: ``one@example.org two@example.org``.
  Fixes https://github.com/collective/Products.PrintingMailHost/issues/4
  [maurits]


0.8 (2015-04-16)
----------------

- Add environment variable ``PRINTING_MAILHOST_FIXED_ADDRESS`` to send
  all emails to a single, fixed address.  PrintingMailHost still needs
  to be enabled, so this is in addition to printing.
  https://github.com/collective/Products.PrintingMailHost/issues/2
  [maurits]

- Since we can enable PMH via an environment variable and thus when not
  running in debug mode / foreground, emails are no longer printed, but
  written to the zope event log.
  [pysailor]


0.7 (2010-01-05)
----------------

- Also patch (Secure)MaildropHost when available.
  [maurits]


0.6 (2010-01-05)
----------------

- Allow passing keyword 'immediate'.  Needed for Plone 4 compatibility.
  [maurits]


0.5 (2009-08-07)
----------------

- Fix email Message import
  [claytron]


0.4 (2009-07-24)
----------------

- Rough support for multipart email messages
  [iElectric]


0.3 (2009-03-22)
----------------

- Decode base64 encoded email messages
  [claytron]

- Added environment variable (ENABLE_PRINTING_MAILHOST) to enable
  or disable PrintingMailHost
  [claytron]

- Update README and HISTORY.txt
  [claytron]


0.2 (2008-08-20)
----------------

- Release as an egg to PyPi
  [claytron]


0.1
---

- Updated to use the new standard log mechanism: logging.getLogger.
  Reformated messages/docstrings.
  [dtremea] (2006-03-17)

- Extended to also patch SecureMailBase from SecureMailHost, if
  available.
  [dtremea] (2005-10-23)

- Fixed to work both with old-style and new-style classes, as in
  the later, dict is a 'dictproxy' instance, which doesn't have the
  setitem method. Bumpped version. Noted changes. And clean up
  whitespaces, of course... ;-)
  [dtremea] (2005-10-23)

- Initial creation/release
  [optilude] (2005-04-05)
