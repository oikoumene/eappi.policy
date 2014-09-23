from setuptools import setup, find_packages
import os

version = '1.10.dev0'

setup(name='eappi.policy',
      version=version,
      description="",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.rst")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Inigo Consulting',
      author_email='team@inigo-tech.com',
      url='http://github.com/inigoconsulting/',
      license='gpl',
      packages=find_packages(),
      namespace_packages=['eappi'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.dexterity [grok, relations]',
          'plone.namedfile [blobs]',
          'collective.grok',
          'plone.app.referenceablebehavior',
          'collective.dexteritytextindexer',
          'plone.app.multilingual',
          'plone.multilingualbehavior',
          'eappi.theme',
          'wcc.homepage',
          'wcc.common',
          'Products.ContentWellPortlets',
          'collective.socialbar',
          'Products.RedirectionTool',
          'wcc.featurable',
          'collective.portlet.collectionmultiview',
          'collective.documentviewer',
          'collective.captchacontactinfo',
          'ftw.blog',
          'collective.js.unslider',
          'collective.sliderfields',
          'wcc.multilingual',
          'eappi.map',
          'wcc.rawhtml',
          'collective.plonetruegallery',
          'redturtle.video',
          'collective.rtvideo.youtube',
          'collective.rtvideo.vimeo',
          'wcc.video',
          'wcc.videolink',
          'Products.PloneFormGen',
          'eappi.customrss',
          # -*- Extra requirements: -*-
      ],
      extras_require={
          'test': [
              'plone.app.testing',
           ],
      },
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      # The next two lines may be deleted after you no longer need
      # addcontent support from paster and before you distribute
      # your package.
      setup_requires=["PasteScript"],
      paster_plugins=["templer.localcommands"],

      )
