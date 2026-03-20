from Products.CMFCore.utils import getToolByName
from Products.PrintingMailHost.testing import PRINTINGMAILHOST_INTEGRATION_TESTING

import unittest


class TestIntegration(unittest.TestCase):
    layer = PRINTINGMAILHOST_INTEGRATION_TESTING

    def test_add_missing_uuids(self):
        mailhost = getToolByName(self.layer["portal"], "MailHost")
        with self.assertLogs("PrintingMailHost", level="INFO") as logs:
            mailhost.send(
                "message text",
                mfrom="me@example.org",
                mto="you@example.org",
                subject="Hello",
                immediate=True,
            )
            self.assertEqual(len(logs.output), 1)
            output = logs.output[0]
            self.assertIn("From: me@example.org", output)
            self.assertIn("To: you@example.org", output)
            self.assertIn("Subject: Hello", output)
            self.assertIn("message text", output)
