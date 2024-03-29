compile:
	copy fannkuchredux.hipe fannkuchredux.erl
	erlc fannkuchredux.erl
measure:
	cmd /C start /B cmd /C "scaphandre json -n 100000 -f fannkuchredux-main-12.json >NUL 2>NUL"
	timeout /T 5 /NOBREAK > NUL
	erl -smp enable -noshell -run  fannkuchredux main 12
	timeout /T 5 /NOBREAK > NUL
	taskkill /F /IM scaphandre.exe
run:
	erl -smp enable -noshell -run  fannkuchredux main 12
clean:
	del /Q *.json *.beam *.erl *.dump
