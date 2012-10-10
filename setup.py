from setuptools import setup, find_packages
import os

version = '1.0'
shortdesc = 'multiselect widget for YAFOWIL'
longdesc = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
longdesc += open(os.path.join(os.path.dirname(__file__), 'HISTORY.rst')).read()
longdesc += open(os.path.join(os.path.dirname(__file__), 'LICENSE.rst')).read()
tests_require = ['yafowil[test]']

setup(name='yafowil.widget.multiselect',
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
      url=u'http://pypi.python.org/pypi/yafowil.widget.multiselect',
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
      test_suite="yafowil.widget.multiselect.tests.test_suite",
      entry_points="""
      [yafowil.plugin]
      register = yafowil.widget.multiselect:register
      example = yafowil.widget.multiselect.example:get_example
      """,
      )

