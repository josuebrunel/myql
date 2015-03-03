##################################################
#
#   Author          : yosuke
#   Filename        : run_tests.sh
#   Description     :
#   Creation Date   : 03-03-2015
#   Last Modified   : Tue 03 Mar 2015 07:03:37 AM CST
#
##################################################

if [ ! -z $1 ]; then
    test=".$1"
fi

python -m unittest "tests.LokingYqlTest${test}"
