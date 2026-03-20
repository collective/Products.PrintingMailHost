from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import zope

import os


class PrintingMailHostFixture(PloneSandboxLayer):
    # defaultBases = (AUTOLOGIN_LIBRARY_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        os.environ["ENABLE_PRINTING_MAILHOST"] = "yes"
        zope.installProduct(app, "Products.PrintingMailHost")


PRINTINGMAILHOST_FIXTURE = PrintingMailHostFixture()

PRINTINGMAILHOST_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PRINTINGMAILHOST_FIXTURE,), name="PrintingMailHost:Integration"
)
