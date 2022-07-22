#!/bin/bash

torsocks on
torsocks on
torsocks on
torsocks on

if ($6 == 1) then
	python WiDoS.py -a $1 -T $2 -c $3 -t $4 --no_stop
else then
	python WiDoS.py -a $1 -T $2 -c $3 -t $4 -L $6
fi
