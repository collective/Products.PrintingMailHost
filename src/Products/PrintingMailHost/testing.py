from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import zope


class PrintingMailHostFixture(PloneSandboxLayer):
    # defaultBases = (AUTOLOGIN_LIBRARY_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        zope.installProduct(app, "Products.PrintingMailHost")

    def tearDownZope(self, app):
        from Products.PrintingMailHost.Patch import undo_patches

        undo_patches()
        zope.uninstallProduct(app, "Products.PrintingMailHost")


PRINTINGMAILHOST_FIXTURE = PrintingMailHostFixture()

PRINTINGMAILHOST_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PRINTINGMAILHOST_FIXTURE,), name="PrintingMailHost:Integration"
)
