from pathlib import Path
from setuptools import setup


long_description = Path("README.md").read_text() + "\n" + Path("CHANGES.md").read_text()

version = "2.0.1.dev0"

setup(
    name="Products.PrintingMailHost",
    version=version,
    description="A monkey patch to send MailHost messages to standard out",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Plone",
        "Framework :: Plone :: 6.2",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="zope debug mailhost",
    author="Martin Aspeli",
    author_email="plone-developers@lists.sourceforge.net",
    url="https://github.com/collective/Products.PrintingMailHost",
    license="GPL",
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.10",
    install_requires=[
        "Products.MailHost",
        "Zope",
    ],
)
