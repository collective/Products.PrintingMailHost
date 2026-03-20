from Products.CMFCore.utils import getToolByName
from Products.PrintingMailHost.testing import PRINTINGMAILHOST_INTEGRATION_TESTING

import unittest


class TestIntegration(unittest.TestCase):
    layer = PRINTINGMAILHOST_INTEGRATION_TESTING

    def send(self):
        mailhost = getToolByName(self.layer["portal"], "MailHost")
        mailhost.send(
            "message text",
            mfrom="me@example.org",
            mto="you@example.org",
            subject="Hello",
            immediate=True,
        )

    def test_output(self):
        with self.assertLogs("PrintingMailHost", level="INFO") as logs:
            self.send()
            self.assertEqual(len(logs.output), 1)
            output = logs.output[0]
            self.assertIn("From: me@example.org", output)
            self.assertIn("To: you@example.org", output)
            self.assertIn("Subject: Hello", output)
            self.assertIn("message text", output)

    def test_unpatch(self):
        from Products.PrintingMailHost.Patch import undoPatches

        undoPatches()
        with self.assertNoLogs("PrintingMailHost", level="INFO"):
            with self.assertRaises(ConnectionRefusedError):
                self.send()
