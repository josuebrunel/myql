##################################################
#
#   Author          : josuebrunel
#   Filename        : publish_package.sh
#   Description     :
#   Creation Date   : 03-05-2015
#   Last Modified   : Sun May  3 14:55:43 2015
#
##################################################

if [ ! -z $1 ]; then
    if [ $1 == 'testing' ]
        $server=pypitest
    else
        $server=pypi
fi

python setup.py register -r $sever

python setup.py sdist upload -r $server
