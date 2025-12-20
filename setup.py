from pathlib import Path
from setuptools import find_packages
from setuptools import setup


long_description = Path("README.md").read_text() + "\n" + Path("CHANGES.md").read_text()

version = "1.1.9.dev0"

setup(
    name="Products.PrintingMailHost",
    version=version,
    description="A monkey patch to send MailHost messages to standard out",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Plone",
        "Framework :: Plone :: 4.3",
        "Framework :: Plone :: 5.0",
        "Framework :: Plone :: 5.1",
        "Framework :: Plone :: 5.2",
        "Framework :: Plone :: 6.0",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="zope debug mailhost",
    author="Martin Aspeli",
    author_email="plone-developers@lists.sourceforge.net",
    url="https://github.com/collective/Products.PrintingMailHost",
    license="GPL",
    packages=find_packages("src"),
    namespace_packages=["Products"],
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    python_requires=">=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*,!=3.5.*",
    install_requires=[
        "setuptools",
        "Products.MailHost",
        "Zope",
    ],
)
