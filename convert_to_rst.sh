##################################################
#
#   Author          : josuebrunel
#   Filename        : convert_to_rst.sh
#   Description     : use pandoc to convert md file to rst
#   Creation Date   : 10-05-2015
#   Last Modified   : Thu 21 May 2015 11:17:35 AM CEST
#
##################################################

rm -rf index.html
wget http://myql.readthedocs.org/en/latest/index.html
pandoc index.html -t rst -o README.rst
