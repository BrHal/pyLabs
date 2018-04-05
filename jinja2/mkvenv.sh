#!/bin/bash
venvDir=~/venvs/jinja2
echo "set your virtualenv - source $venvDir/bin/activate"
[ -d ${venvDir} ] && exit 0
virtualenv $venvDir
. $venvDir/bin/activate
pip install jinja2
