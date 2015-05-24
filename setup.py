import os
from setuptools import setup, find_packages

__version__ = "1.2.2"

#requirements.txt
with open('requirements.txt') as f:
  required = f.read().splitlines()

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
  name = "mYQL",
  version = __version__,
  description = "Python Wrapper for the Yahoo! Query Language",
  long_description = read("README.rst"),
  author = "Josue Kouka",
  author_email = "josuebrunel@gmail.com",
  url = "https://github.com/josuebrunel/MYQL",
  download_url = "https://github.com/josuebrunel/myql/archive/{0}.tar.gz".format(__version__),
  keywords = ['myql', 'yql', 'yahoo', 'query', 'language'],
  packages = find_packages(),
  classifiers = [
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Development Status :: 5 - Stable',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License'
  ],
  platforms=['Any'],
  license='MIT',
  install_requires = required
)
