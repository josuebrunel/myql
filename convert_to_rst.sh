##################################################
#
#   Author          : josuebrunel
#   Filename        : convert_to_rst.sh
#   Description     : use pandoc to convert md file to rst
#   Creation Date   : 10-05-2015
#   Last Modified   : Wed 20 May 2015 11:47:17 AM CEST
#
##################################################


wget http://myql.readthedocs.org/en/latest/index.html
pandoc index.html -t rst -o README.rst
