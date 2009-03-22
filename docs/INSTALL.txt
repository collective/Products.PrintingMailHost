Products.PrintingMailHost Installation
======================================

To install Products.PrintingMailHost into the global Python environment (or a workingenv),
using a traditional Zope 2 instance, you can do this:

- When you're reading this you have probably already run 
  ``easy_install Products.PrintingMailHost``. Find out how to install setuptools
  (and EasyInstall) here:
  http://peak.telecommunity.com/DevCenter/EasyInstall

Alternatively, if you are using zc.buildout and the plone.recipe.zope2instance
recipe to manage your project, you can do this:

- Add ``Products.PrintingMailHost`` to the list of eggs to install, e.g.::

    [buildout]
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

- Re-run buildout in order to make any of the above changes active::

    $ ./bin/buildout
