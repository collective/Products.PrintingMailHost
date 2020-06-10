from setuptools import setup, find_packages

version = '1.1.4'

setup(name='Products.PrintingMailHost',
      version=version,
      description="A monkey patch to send MailHost messages to standard out",
      long_description=(open("README.rst").read() + '\n\n' +
                        open('CHANGES.rst').read()),
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Framework :: Plone",
          "Framework :: Plone :: 4.3",
          "Framework :: Plone :: 5.0",
          "Framework :: Plone :: 5.1",
          "Framework :: Plone :: 5.2",
          "License :: OSI Approved :: GNU General Public License (GPL)",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
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
          'six',
      ],
      )
