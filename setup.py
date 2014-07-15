from setuptools import setup, find_packages

version = '0.8dev'

setup(name='Products.PrintingMailHost',
      version=version,
      description="A monkey patch to send MailHost messages to standard out",
      long_description=(open("README.rst").read() + '\n\n' +
                        open('CHANGES.rst').read()),
      classifiers=[
          "Framework :: Plone",
          "Programming Language :: Python",
          "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      keywords='zope debug mailhost',
      author='Martin Aspeli',
      author_email='plone-developers@lists.sourceforge.net',
      url='http://svn.plone.org/svn/collective/Products.PrintingMailHost',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['Products'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
