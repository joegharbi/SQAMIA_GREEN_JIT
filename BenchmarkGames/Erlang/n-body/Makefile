compile:
	copy nbody.hipe-3.hipe nbody.erl
	erlc nbody.erl
measure:
	cmd /C start /B cmd /C "scaphandre json -n 100000 -f nbody-main-50000000.json >NUL 2>NUL"
	timeout /T 5 /NOBREAK > NUL
	erl -smp enable -noshell -run  nbody main 50000000
	timeout /T 5 /NOBREAK > NUL
	taskkill /F /IM scaphandre.exe
run:
	erl -smp enable -noshell -run  nbody main 50000000
clean:
	del /Q *.json *.beam *.erl *.dump