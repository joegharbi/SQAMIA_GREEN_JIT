compile:
	cp fannkuchredux.hipe fannkuchredux.erl
	erlc fannkuchredux.erl

measure:
	scaphandre json -n 100000 -f fannkuchredux-main-12.json >/dev/null 2>&1 &
	sleep 5
	erl -smp enable -noshell -run  fannkuchredux main 12
	sleep 5
	pkill -f scaphandre

run:
	erl -smp enable -noshell -run  fannkuchredux main 12

clean:
	rm -f *.json *.beam *.erl *.dump
