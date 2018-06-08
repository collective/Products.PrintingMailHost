from setuptools import setup, find_packages

version = '1.1.0'

setup(name='Products.PrintingMailHost',
      version=version,
      description="A monkey patch to send MailHost messages to standard out",
      long_description=(open("README.rst").read() + '\n\n' +
                        open('CHANGES.rst').read()),
      classifiers=[
          "Framework :: Plone",
          "Framework :: Plone :: 3.3",
          "Framework :: Plone :: 4.0",
          "Framework :: Plone :: 4.1",
          "Framework :: Plone :: 4.2",
          "Framework :: Plone :: 4.3",
          "Framework :: Plone :: 5.0",
          "Framework :: Plone :: 5.1",
          "License :: OSI Approved :: GNU General Public License (GPL)",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.4",
          "Programming Language :: Python :: 2.6",
          "Programming Language :: Python :: 2.7",
          "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      keywords='zope debug mailhost',
      author='Martin Aspeli',
      author_email='plone-developers@lists.sourceforge.net',
      url='https://github.com/collective/Products.PrintingMailHost',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['Products'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
      ],
      )
