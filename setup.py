import os
from setuptools import setup, find_packages

__version__ = "1.2.1"

#requirements.txt
with open('requirements.txt') as f:
  required = f.read().splitlines()

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
  name = "myql",
  version = __version__,
  description = "Python Wrapper for the Yahoo ! Query Language",
  long_description = read("README.rst"),
  author = "Josue Kouka",
  author_email = "josuebrunel@gmail.com",
  url = "https://github.com/josuebrunel/MYQL",
  download_url = "https://github.com/josuebrunel/myql/archives/{0}tar.gz".format(__version__),
  keywords = ['myql', 'yql', 'yahoo', 'query', 'language'],
  packages = find_packages(),
  classifiers = [
    'Programming Language :: Python :: 2.7',
    'Development Status :: 4 - Beta',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License'
  ],
  platforms=['Any'],
  license='BSD',
  install_requires = required
)
