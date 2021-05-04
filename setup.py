from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='pybamcmap',
      version='0.3.1',
      description='A collection of colormaps using the CD of the Bundesanstalt für Materialforschung und -prüfung (BAM).',
      url='https://github.com/dhufe/pybamcmap',
      author='Daniel Hufschläger',
      author_email='daniel@hufschlaeger.net',
      license='MIT',
      packages=['pybamcmap'],
      long_description = long_description,
      long_description_content_type = 'text/markdown',
      zip_safe=False)
