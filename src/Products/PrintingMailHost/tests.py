from Products.CMFCore.utils import getToolByName
from Products.PrintingMailHost.testing import PRINTINGMAILHOST_INTEGRATION_TESTING

import unittest


class TestIntegration(unittest.TestCase):
    layer = PRINTINGMAILHOST_INTEGRATION_TESTING

    def setUp(self) -> None:
        from Products.PrintingMailHost.Patch import apply_patches

        apply_patches()
        return super().setUp()

    def tearDown(self) -> None:
        from Products.PrintingMailHost.Patch import undo_patches

        undo_patches()
        return super().tearDown()

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

    def test_fixed_address(self):
        from Products.PrintingMailHost import Patch

        orig_fixed_address = Patch.FIXED_ADDRESS
        Patch.FIXED_ADDRESS = ["another@example.org"]
        try:
            with self.assertLogs("PrintingMailHost", level="INFO") as logs:
                with self.assertRaises(ConnectionRefusedError):
                    self.send()
                self.assertEqual(len(logs.output), 2)
                output = logs.output[0]
                self.assertIn("From: me@example.org", output)
                self.assertIn("To: you@example.org", output)
                self.assertIn("Subject: Hello", output)
                self.assertIn("message text", output)
                self.assertIn(
                    "Sending actual email to ['another@example.org']", logs.output[1]
                )
        finally:
            Patch.FIXED_ADDRESS = orig_fixed_address

    def test_unpatch(self):
        from Products.PrintingMailHost.Patch import undo_patches

        undo_patches()
        with self.assertNoLogs("PrintingMailHost", level="INFO"):
            with self.assertRaises(ConnectionRefusedError):
                self.send()
