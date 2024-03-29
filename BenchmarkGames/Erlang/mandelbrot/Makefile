compile:
	copy mandelbrot.hipe-2.hipe mandelbrot.erl
	erlc mandelbrot.erl
measure:
	cmd /C start /B cmd /C "cmd /C start /B scaphandre json -n 100000 -f mandelbrot-main-16000.json >NUL 2>NUL"
	timeout /T 5 /NOBREAK > NUL
	erl -smp enable -noshell -run  mandelbrot main 16000
	timeout /T 5 /NOBREAK > NUL
	taskkill /F /IM scaphandre.exe
run:
	erl -smp enable -noshell -run  mandelbrot main 16000
clean:
	del /Q *.json *.beam *.erl *.dump