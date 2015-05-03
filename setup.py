from setuptools import setup, find_packages

#requirements.txt
with open('requirements.txt') as f:
  required = f.read().splitlines()

setup(
  name = "myql",
  version = "1.2",
  description = "Python Wrapper for the Yahoo ! Query Language",
  long_description = "",
  author = "Josue Kouka",
  author_email = "josuebrunel@gmail.com",
  url = "https://github.com/josuebrunel/MYQL",
  download_url = "https://github.com/josuebrunel/myql/tarball/1.2",
  keywords = ['myql', 'yql', 'yahoo', 'query', 'language'],
  packages = find_packages(),
  platforms=['Any'],
  license='BSD',
  install_requires = required
)
