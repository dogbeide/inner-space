#!/bin/bash



if [ ${PWD##*/} != 'tools' ] && [ ${PWD##*/} != 'inner-space' ]
then
  # run script
  echo -e "\nERROR: Must run script from either 'inner-space' project root or 'inner-space/tools'\n"
  exit
elif [ ${PWD##*/} = 'tools' ]
then
  cd ..
fi

python -Wall manage.py test

: '
# TODO:

start server
close server

innerspace urls & views
accounts.tests.py
posts.tests.py
comments.tests.py

'
