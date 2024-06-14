compile:
	cp revcomp.hipe revcomp.erl
	erlc revcomp.erl
measure:
	scaphandre json -n 100000 -f revcomp-main-0.json >/dev/null 2>&1 &
	sleep 5
	erl -smp enable -noshell -run  revcomp main 0 < ../../revcomp-input25000000.txt
	sleep 5
	pkill -f scaphandre
run:
	erl -smp enable -noshell -run  revcomp main 0 < ../../revcomp-input25000000.txt
clean:
	rm -f *.json *.beam *.erl *.dump