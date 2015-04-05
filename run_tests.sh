##################################################
#
#   Author          : yosuke
#   Filename        : run_tests.sh
#   Description     :
#   Creation Date   : 03-03-2015
#   Last Modified   : Sun 05 Apr 2015 01:46:24 AM CEST
#
##################################################

if [ ! -z $1 ]; then
    test=".$1"
fi

python -m unittest "tests.LokingYqlTest${test}"
