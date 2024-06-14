compile:
	cp nbody.hipe-3.hipe nbody.erl
	erlc nbody.erl

measure:
	scaphandre json -n 100000 -f nbody-main-50000000.json >/dev/null 2>&1 &
	sleep 5
	erl -smp enable -noshell -run  nbody main 50000000
	sleep 5
	pkill -f scaphandre

run:
	erl -smp enable -noshell -run  nbody main 50000000

clean:
	rm -f *.json *.beam *.erl *.dump
