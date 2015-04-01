from setuptools import setup, find_packages

#requirements.txt
with open('requirements.txt') as f:
  required = f.read().splitlines()

setup(
  name = "lokingyql",
  version = "0.5",
  description = "Python Wrapper for the Yahoo ! Query Language",
  long_description = "",
  author = "Josue Kouka",
  author_email = "josuebrunel@gmail.com",
  url = "https://github.com/josuebrunel/lokingYQL",
  packages = find_packages,
  platforms=['Any'],
  license='BSD',
  install_requires = required
)
