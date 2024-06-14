compile:
	cp mandelbrot.hipe-2.hipe mandelbrot.erl
	erlc mandelbrot.erl

measure:
	scaphandre json -n 100000 -f mandelbrot-main-16000.json >/dev/null 2>&1 &
	sleep 5
	erl -smp enable -noshell -run mandelbrot main 16000
	sleep 5
	pkill -f scaphandre

run:
	erl -smp enable -noshell -run mandelbrot main 16000

clean:
	rm -f *.json *.beam *.erl *.dump
