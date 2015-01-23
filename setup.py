import os
from setuptools import (
    setup,
    find_packages,
)

version = '1.1'
shortdesc = 'Chosen select/autocomplete widget for YAFOWIL'
longdesc = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
longdesc += open(os.path.join(os.path.dirname(__file__), 'HISTORY.rst')).read()
longdesc += open(os.path.join(os.path.dirname(__file__), 'LICENSE.rst')).read()
tests_require = ['yafowil[test]']


setup(name='yafowil.widget.chosen',
      version=version,
      description=shortdesc,
      long_description=longdesc,
      classifiers=[
          'Environment :: Web Environment',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
          'License :: OSI Approved :: BSD License',
      ],
      keywords='',
      author='BlueDynamics Alliance',
      author_email='dev@bluedynamics.com',
      url=u'https://github.com/bluedynamics/yafowil.widget.chosen',
      license='Simplified BSD',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['yafowil', 'yafowil.widget'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'yafowil>1.99',
      ],
      tests_require=tests_require,
      extras_require = dict(
          test=tests_require,
      ),
      test_suite="yafowil.widget.chosen.tests.test_suite",
      entry_points="""
      [yafowil.plugin]
      register = yafowil.widget.chosen:register
      example = yafowil.widget.chosen.example:get_example
      """)
